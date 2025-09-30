from __future__ import annotations
import os
import re
import shlex
from contextlib import contextmanager
from typing import Any, Dict, Generator, List, Tuple

import click
import requests
import yaml
import tempfile

from pyhelper_utils.shell import run_command
from simple_logger.logger import get_logger

from openshift_cli_installer.libs.clusters.ocp_cluster import OCPCluster
from openshift_cli_installer.libs.user_input import UserInput
from openshift_cli_installer.utils.cluster_versions import (
    get_cluster_version_to_install,
    get_ipi_cluster_versions,
    parse_openshift_release_url,
)
from openshift_cli_installer.utils.const import CREATE_STR, DESTROY_STR, PRODUCTION_STR, GCP_STR, AWS_STR
from openshift_cli_installer.utils.general import (
    generate_unified_pull_secret,
    get_install_config_j2_template,
    get_local_ssh_key,
    zip_and_upload_to_s3,
)
from openshift_cli_installer.utils.general import get_dict_from_json


class IpiCluster(OCPCluster):
    def __init__(self, ocp_cluster: Dict[str, Any], user_input: UserInput) -> None:
        super().__init__(ocp_cluster=ocp_cluster, user_input=user_input)
        self.logger = get_logger(f"{self.__class__.__module__}-{self.__class__.__name__}")
        self.log_level = self.cluster.get("log_level", "error")

        self.platform = ""
        self.gcp_project_id = ""
        self.unified_pull_secret = generate_unified_pull_secret(
            registry_config_file=self.user_input.registry_config_file,
            docker_config_file=self.user_input.docker_config_file,
        )
        self.fips = self.cluster_info.get("fips")
        if self.fips:
            self.fips = True if self.fips.lower() == "true" else False
            os.environ["OPENSHIFT_INSTALL_SKIP_HOSTCRYPT_VALIDATION"] = "true"

        if self.user_input.destroy_from_s3_bucket_or_local_directory:
            self._ipi_download_installer()
        else:
            self.openshift_install_binary_path = ""
            self.ipi_base_available_versions: Dict[str, Dict[str, List[str]]]
            self.cluster["ocm-env"] = self.cluster_info["ocm-env"] = PRODUCTION_STR

    def _prepare_ipi_cluster(self) -> None:
        self.ipi_base_available_versions = get_ipi_cluster_versions()
        self.cluster["version"] = get_cluster_version_to_install(
            wanted_version=self.cluster_info["user-requested-version"],
            base_versions_dict=self.ipi_base_available_versions,
            platform=self.cluster_info["platform"],
            stream=self.cluster_info["stream"],
            log_prefix=self.log_prefix,
        )
        self._set_install_version_url()
        self._ipi_download_installer()
        if self.user_input.create:
            self._create_install_config_file()

    def _ipi_download_installer(self) -> None:
        openshift_install_binary = f"openshift-install{'-fips' if self.fips else ''}"
        version_url = self.cluster_info["version-url"]
        binary_dir = os.path.join(tempfile.TemporaryDirectory().name, version_url)
        self.openshift_install_binary_path = os.path.join(binary_dir, openshift_install_binary)

        with self._set_docker_config_file() as unified_pull_secret:
            rc, _, err = run_command(
                command=shlex.split(
                    "oc adm release extract "
                    f"{version_url} "
                    f"--command={openshift_install_binary} --to={binary_dir} --registry-config={unified_pull_secret}"
                ),
                check=False,
            )

            if not rc:
                self.logger.error(
                    f"{self.log_prefix}: Failed to get {openshift_install_binary} for version {version_url}, error: {err}",
                )
                raise click.Abort()

    def _create_install_config_file(self) -> None:
        terraform_parameters = {
            "name": self.cluster_info["name"],
            "region": self.cluster_info["region"],
            "base_domain": self.cluster_info["base-domain"],
            "platform": self.cluster_info["platform"],
            "ssh_key": get_local_ssh_key(ssh_key_file=self.user_input.ssh_key_file),
            "pull_secret": self.unified_pull_secret,
        }

        if worker_flavor := self.cluster.get("worker-flavor"):
            terraform_parameters["worker_flavor"] = worker_flavor

        if worker_root_disk_size := self.cluster.get("worker-root-disk-size"):
            terraform_parameters["worker_root_disk_size"] = worker_root_disk_size

        if worker_replicas := self.cluster.get("worker-replicas"):
            terraform_parameters["worker_replicas"] = worker_replicas

        if self.gcp_project_id:
            terraform_parameters["gcp_project_id"] = self.gcp_project_id

        if fips := self.cluster.get("fips"):
            terraform_parameters["fips"] = fips

        cluster_install_config = get_install_config_j2_template(jinja_dict=terraform_parameters, platform=self.platform)

        with open(os.path.join(self.cluster_info["cluster-dir"], "install-config.yaml"), "w") as fd:
            fd.write(yaml.dump(cluster_install_config))

    @contextmanager
    def _set_docker_config_file(self) -> Generator[str, None, None]:
        with tempfile.NamedTemporaryFile(prefix="pull-secret-") as fp:
            fp.write(bytes(self.unified_pull_secret, "utf-8"))
            yield fp.name

    def _set_install_version_url(self) -> None:
        version_url = None
        cluster_version = self.cluster["version"]
        for tr in parse_openshift_release_url():
            version = any(_tr for _tr in tr.text.splitlines() if cluster_version == _tr)
            if version:
                href = tr.find_all("a", attrs={"class": "text-success"})[0]["href"]
                version_url_match = re.search(
                    r"oc adm release extract --tools (.*?)<",
                    requests.get(f"https://{[*self.ipi_base_available_versions][0]}{href}").text,
                )
                version_url = version_url_match.group(1) if version_url_match else None

        if version_url:
            self.cluster_info["version-url"] = version_url
        else:
            self.logger.error(
                f"{self.log_prefix}: Cluster version url not found for"
                f" {cluster_version} in {self.ipi_base_available_versions.keys()}",
            )
            raise click.Abort()

    def run_installer_command(self, action: str, raise_on_failure: bool) -> Tuple[bool, str, str]:
        run_after_failed_create_str = (
            " after cluster creation failed" if action == DESTROY_STR and self.user_input.action == CREATE_STR else ""
        )
        self.logger.info(f"{self.log_prefix}: Running cluster {action}{run_after_failed_create_str}")
        res, out, err = run_command(
            command=shlex.split(
                f"{self.openshift_install_binary_path} {action} cluster --dir"
                f" {self.cluster_info['cluster-dir']} --log-level {self.log_level}"
            ),
            capture_output=False,
            check=False,
        )

        if not res:
            self.logger.error(
                f"{self.log_prefix}: Failed to run cluster {action} \n\tERR: {err}\n\tOUT: {out}.",
            )
            if raise_on_failure:
                raise click.Abort()

        return res, out, err

    def create_cluster(self) -> None:
        def _rollback_on_error(_ex: Exception | None = None) -> None:
            self.logger.error(f"{self.log_prefix}: Failed to create cluster: {_ex or 'No exception'}")
            if self.user_input.must_gather_output_dir:
                self.collect_must_gather()

            self.logger.warning(f"{self.log_prefix}: Cleaning cluster leftovers.")
            self.destroy_cluster()
            raise click.Abort()

        self.timeout_watch = self.start_time_watcher()
        res, _, _ = self.run_installer_command(action=CREATE_STR, raise_on_failure=False)

        if not res:
            _rollback_on_error()

        try:
            self.add_cluster_info_to_cluster_object()
            self.logger.success(f"{self.log_prefix}: Cluster created successfully")

        except Exception as ex:
            _rollback_on_error(_ex=ex)

        if self.user_input.s3_bucket_name:
            zip_and_upload_to_s3(
                install_dir=self.cluster_info["cluster-dir"],
                s3_bucket_name=self.user_input.s3_bucket_name,
                s3_bucket_object_name=self.cluster_info["s3-object-name"],
            )

    def destroy_cluster(self) -> None:
        self.timeout_watch = self.start_time_watcher()
        self.run_installer_command(action=DESTROY_STR, raise_on_failure=True)
        self.logger.success(f"{self.log_prefix}: Cluster destroyed")
        self.delete_cluster_s3_buckets()


class AwsIpiCluster(IpiCluster):
    def __init__(self, ocp_cluster: Dict[str, Any], user_input: UserInput) -> None:
        super().__init__(ocp_cluster=ocp_cluster, user_input=user_input)
        self.logger = get_logger(f"{self.__class__.__module__}-{self.__class__.__name__}")
        self.platform = AWS_STR
        if not self.user_input.destroy_from_s3_bucket_or_local_directory:
            self._prepare_ipi_cluster()
            self.dump_cluster_data_to_file()

        self.prepare_cluster_data()


class GcpIpiCluster(IpiCluster):
    def __init__(self, ocp_cluster: Dict[str, Any], user_input: UserInput) -> None:
        super().__init__(ocp_cluster=ocp_cluster, user_input=user_input)
        self.logger = get_logger(f"{self.__class__.__module__}-{self.__class__.__name__}")
        self.platform = GCP_STR
        self.gcp_project_id = get_dict_from_json(gcp_service_account_file=self.user_input.gcp_service_account_file)[
            "project_id"
        ]
        if not self.user_input.destroy_from_s3_bucket_or_local_directory:
            self._prepare_ipi_cluster()
            self.dump_cluster_data_to_file()

        self.prepare_cluster_data()
