from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List

import click
import rosa.cli
from clouds.aws.aws_utils import set_and_verify_aws_credentials
from clouds.gcp.utils import get_gcp_regions
from ocm_python_wrapper.ocm_client import OCMPythonClient
from simple_logger.logger import get_logger

from openshift_cli_installer.libs.clusters.ipi_cluster import (
    AwsIpiCluster,
    GcpIpiCluster,
)
from openshift_cli_installer.libs.clusters.osd_cluster import OsdCluster
from openshift_cli_installer.libs.clusters.rosa_cluster import RosaCluster
from openshift_cli_installer.libs.user_input import UserInput
from openshift_cli_installer.utils.const import (
    AWS_OSD_STR,
    AWS_STR,
    GCP_OSD_STR,
    HYPERSHIFT_STR,
    PRODUCTION_STR,
    ROSA_STR,
    STAGE_STR,
    GCP_STR,
)


class OCPClusters:
    def __init__(self, user_input: UserInput) -> None:
        self.user_input = user_input
        self.logger = get_logger(f"{self.__class__.__module__}-{self.__class__.__name__}")
        self.aws_ipi_clusters: List[AwsIpiCluster] = []
        self.gcp_ipi_clusters: List[GcpIpiCluster] = []
        self.aws_osd_clusters: List[OsdCluster] = []
        self.rosa_clusters: List[RosaCluster] = []
        self.hypershift_clusters: List[RosaCluster] = []
        self.gcp_osd_clusters: List[OsdCluster] = []

        self.s3_target_dirs: List[str] = []

        for _cluster in user_input.clusters:
            self.add_to_cluster_lists(ocp_cluster=_cluster)

        if self.user_input.create:
            self.check_ocm_managed_existing_clusters()
            self.is_region_support_hypershift()
            self.is_region_support_aws()
            self.is_region_support_gcp()

    def add_to_cluster_lists(self, ocp_cluster: Dict[str, Any]) -> None:
        _cluster_platform = ocp_cluster["platform"]
        if _cluster_platform == AWS_STR:
            self.aws_ipi_clusters.append(AwsIpiCluster(ocp_cluster=ocp_cluster, user_input=self.user_input))

        if _cluster_platform == GCP_STR:
            self.gcp_ipi_clusters.append(GcpIpiCluster(ocp_cluster=ocp_cluster, user_input=self.user_input))

        if _cluster_platform == AWS_OSD_STR:
            self.aws_osd_clusters.append(OsdCluster(ocp_cluster=ocp_cluster, user_input=self.user_input))

        if _cluster_platform == ROSA_STR:
            self.rosa_clusters.append(RosaCluster(ocp_cluster=ocp_cluster, user_input=self.user_input))

        if _cluster_platform == HYPERSHIFT_STR:
            self.hypershift_clusters.append(RosaCluster(ocp_cluster=ocp_cluster, user_input=self.user_input))

        if _cluster_platform == GCP_OSD_STR:
            self.gcp_osd_clusters.append(OsdCluster(ocp_cluster=ocp_cluster, user_input=self.user_input))

    @property
    def list_clusters(self) -> List[Any]:
        return (
            self.aws_ipi_clusters
            + self.aws_osd_clusters
            + self.rosa_clusters
            + self.hypershift_clusters
            + self.gcp_osd_clusters
            + self.gcp_ipi_clusters
        )

    @property
    def aws_managed_clusters(self) -> List[Any]:
        return self.rosa_clusters + self.hypershift_clusters + self.aws_osd_clusters

    @property
    def ocm_managed_clusters(self) -> List[Any]:
        return self.aws_managed_clusters + self.gcp_osd_clusters

    def check_ocm_managed_existing_clusters(self) -> None:
        if self.ocm_managed_clusters:
            self.logger.info("Check for existing OCM-managed clusters.")
            existing_clusters_list = []
            for _cluster in self.ocm_managed_clusters:
                if _cluster.cluster_object.exists:
                    existing_clusters_list.append(_cluster.cluster_info["name"])

            if existing_clusters_list:
                self.logger.error(
                    f"At least one cluster already exists: {existing_clusters_list}",
                )
                raise click.Abort()

    @staticmethod
    def _hypershift_regions(ocm_client: OCMPythonClient) -> List[str]:
        rosa_regions = rosa.cli.execute(
            command="list regions",
            aws_region="us-west-2",
            ocm_client=ocm_client,
        )["out"]
        return [region["id"] for region in rosa_regions if region["supports_hypershift"] is True]

    def is_region_support_hypershift(self) -> None:
        if self.hypershift_clusters:
            self.logger.info(f"Check if regions are {HYPERSHIFT_STR}-supported.")
            unsupported_regions = []
            hypershift_regions_dict: Dict[str, List[str]] = {PRODUCTION_STR: [], STAGE_STR: []}
            for _cluster in self.hypershift_clusters:
                region = _cluster.cluster_info["region"]
                ocm_env = _cluster.cluster_info["ocm-env"]
                _hypershift_regions: List[str] = hypershift_regions_dict[ocm_env]
                if not _hypershift_regions:
                    _hypershift_regions = self._hypershift_regions(ocm_client=_cluster.ocm_client)
                    hypershift_regions_dict[ocm_env] = _hypershift_regions

                if region not in _hypershift_regions:
                    unsupported_regions.append(f"Cluster {_cluster.cluster_info['name']}, region: {region}\n")

                if unsupported_regions:
                    self.logger.error(
                        f"The following {HYPERSHIFT_STR} clusters regions are no"
                        f" supported: {unsupported_regions}.\nSupported hypershift"
                        f" regions are: {_hypershift_regions}",
                    )
                    raise click.Abort()

    def is_region_support_aws(self) -> None:
        _clusters = self.aws_ipi_clusters + self.aws_managed_clusters
        if _clusters:
            self.logger.info(f"Check if regions are {AWS_STR}-supported.")
            _regions_to_verify = set()
            for _cluster in self.aws_ipi_clusters + self.aws_managed_clusters:
                _regions_to_verify.add(_cluster.cluster_info["region"])

            for _region in _regions_to_verify:
                set_and_verify_aws_credentials(region_name=_region)

    def is_region_support_gcp(self) -> None:
        if _clusters := self.gcp_ipi_clusters + self.gcp_osd_clusters:
            self.logger.info(f"Check if regions are {GCP_STR}-supported.")
            supported_regions = get_gcp_regions(gcp_service_account_file=self.user_input.gcp_service_account_file)
            unsupported_regions = []
            for _cluster in _clusters:
                cluster_region = _cluster.cluster_info["region"]
                if cluster_region not in supported_regions:
                    unsupported_regions.append(f"cluster: {_cluster.cluster_info['name']}, region: {cluster_region}")

            if unsupported_regions:
                self.logger.error("The following clusters regions are not supported in GCP: {unsupported_regions}")
                raise click.Abort()

    def run_create_or_destroy_clusters(self) -> None:
        futures: List[Any] = []
        action_str = "create_cluster" if self.user_input.create else "destroy_cluster"

        with ThreadPoolExecutor() as executor:
            for cluster in self.list_clusters:
                action_func = getattr(cluster, action_str)
                self.logger.info(
                    f"Executing {self.user_input.action} cluster {cluster.cluster_info['name']} "
                    f"[parallel: {self.user_input.parallel}]"
                )
                if self.user_input.parallel:
                    futures.append(executor.submit(action_func))
                else:
                    action_func()

            if futures:
                self.process_create_destroy_clusters_threads_results(futures=futures)

    def process_create_destroy_clusters_threads_results(self, futures: List[Any]) -> None:
        create_clusters_error = False
        for result in as_completed(futures):
            _exception = result.exception()
            if _exception:
                if self.user_input.create:
                    create_clusters_error = True
                else:
                    raise click.Abort()

        # If one cluster failed to create we want to destroy all clusters
        if create_clusters_error:
            self.user_input.create = False
            self.logger.error("One cluster failed to create, destroying all clusters")
            self.run_create_or_destroy_clusters()
            raise click.Abort()

    def attach_clusters_to_acm_cluster_hub(self) -> None:
        for cluster in self.list_clusters:
            if cluster.cluster_info.get("acm-clusters"):
                cluster.attach_clusters_to_acm_hub(clusters=self)

    def get_cluster_object_by_name(self, name: str) -> Any:
        for _cluster in self.list_clusters:
            if _cluster.cluster_info["name"] == name:
                return _cluster

    def install_acm_on_clusters(self) -> None:
        for _cluster in self.list_clusters:
            if _cluster.cluster_info["acm"]:
                _cluster.install_acm()

    def enable_observability_on_acm_clusters(self) -> None:
        for _cluster in self.list_clusters:
            if _cluster.cluster_info["acm"] and _cluster.cluster_info["acm-observability"]:
                _cluster.enable_observability()
