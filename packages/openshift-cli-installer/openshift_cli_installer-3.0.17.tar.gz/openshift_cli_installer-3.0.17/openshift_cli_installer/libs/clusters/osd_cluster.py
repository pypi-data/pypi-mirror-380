from typing import Any, Dict

import click
from simple_logger.logger import get_logger

from openshift_cli_installer.libs.clusters.ocm_cluster import OcmCluster
from openshift_cli_installer.libs.user_input import UserInput
from openshift_cli_installer.utils.cluster_versions import get_cluster_version_to_install
from openshift_cli_installer.utils.const import AWS_OSD_STR, GCP_OSD_STR
from openshift_cli_installer.utils.general import zip_and_upload_to_s3, get_dict_from_json


class OsdCluster(OcmCluster):
    def __init__(self, ocp_cluster: Dict[str, Any], user_input: UserInput) -> None:
        super().__init__(ocp_cluster, user_input)
        self.logger = get_logger(f"{self.__class__.__module__}-{self.__class__.__name__}")

        if (platform := self.cluster_info["platform"]) == GCP_OSD_STR:
            self.gcp_service_account = get_dict_from_json(
                gcp_service_account_file=self.user_input.gcp_service_account_file
            )

        if self.user_input.create:
            self.cluster_info["aws-account-id"] = self.user_input.aws_account_id
            self.get_osd_versions()
            self.cluster["version"] = get_cluster_version_to_install(
                wanted_version=self.cluster_info["user-requested-version"],
                base_versions_dict=self.osd_base_available_versions_dict,
                platform=platform,
                stream=self.cluster_info["stream"],
                log_prefix=self.log_prefix,
            )

        if self.user_input.destroy_from_s3_bucket_or_local_directory:
            self.dump_cluster_data_to_file()

    def create_cluster(self) -> None:
        self.timeout_watch = self.start_time_watcher()
        try:
            ocp_version = (
                self.cluster["version"]
                if self.cluster_info["channel-group"] == "stable"
                else f"{self.cluster['version']}-{self.cluster_info['channel-group']}"
            )
            provision_osd_kwargs = {
                "wait_for_ready": True,
                "wait_timeout": self.timeout_watch.remaining_time(),
                "region": self.cluster_info["region"],
                "ocp_version": ocp_version,
                "replicas": self.cluster_info["replicas"],
                "compute_machine_type": self.cluster_info["compute-machine-type"],
                "multi_az": self.cluster_info["multi-az"],
                "channel_group": self.cluster_info["channel-group"],
                "platform": self.cluster_info["platform"].replace("-osd", ""),
            }

            expiration_time = self.cluster_info.get("expiration-time")
            if expiration_time:
                provision_osd_kwargs["expiration_time"] = expiration_time

            if self.cluster_info["platform"] == AWS_OSD_STR:
                provision_osd_kwargs.update({
                    "aws_access_key_id": self.cluster_info["aws-access-key-id"],
                    "aws_account_id": self.cluster_info["aws-account-id"],
                    "aws_secret_access_key": self.cluster_info["aws-secret-access-key"],
                })
            elif self.cluster_info["platform"] == GCP_OSD_STR:
                provision_osd_kwargs.update({"gcp_service_account": self.gcp_service_account})

            self.cluster_object.provision_osd(**provision_osd_kwargs)
            self.add_cluster_info_to_cluster_object()
            self.set_cluster_auth()

            self.logger.success(f"{self.log_prefix}: Cluster created successfully")

        except Exception as ex:
            self.logger.error(
                f"{self.log_prefix}: Failed to run cluster create \n{ex}",
            )
            self.set_cluster_auth()

            if self.user_input.must_gather_output_dir:
                self.collect_must_gather()

            self.destroy_cluster()
            raise click.Abort()

        if self.s3_bucket_name:
            zip_and_upload_to_s3(
                install_dir=self.cluster_info["cluster-dir"],
                s3_bucket_name=self.s3_bucket_name,
                s3_bucket_object_name=self.cluster_info["s3-object-name"],
            )

    def destroy_cluster(self) -> None:
        self.timeout_watch = self.start_time_watcher()
        try:
            self.cluster_object.delete(timeout=self.timeout_watch.remaining_time())
            self.logger.success(f"{self.log_prefix}: Cluster destroyed successfully")
            self.delete_cluster_s3_buckets()
        except Exception as ex:
            self.logger.error(f"{self.log_prefix}: Failed to run cluster destroy\n{ex}")
            raise click.Abort()
