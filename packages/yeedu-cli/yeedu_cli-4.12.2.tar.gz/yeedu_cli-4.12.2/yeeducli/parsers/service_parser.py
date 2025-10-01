from yeeducli.parsers.metastore_catalog.metastore_tenant_secret_parser import MetastoreTenantSecretParser
from yeeducli.parsers.metastore_catalog.metastore_catalog_parser import MetastoreCatalogParser
from yeeducli.parsers.metastore_catalog.metastore_user_secret_parser import MetastoreUserSecretParser
from yeeducli.parsers.metastore_catalog.metastore_workspace_secret_parser import MetastoreWorkspaceSecretParser
from yeeducli.parsers.resource.boot_disk_image_config_parser import BootDiskImageConfigurationParser
from yeeducli.parsers.resource.network_conf_parser import NetworkConfigurationParser
from yeeducli.parsers.resource.volume_conf_parser import VolumeConfigurationParser
from yeeducli.parsers.resource.credentials_conf_parser import CredentialsConfigurationParser
from yeeducli.parsers.resource.cloud_environment_parser import CloudEnvironmentParser
from yeeducli.parsers.resource.object_storage_manager_parser import ObjectStorageManagerParser
from yeeducli.parsers.resource.object_storage_manager_files_parser import ObjectStorageManagerFilesParser
from yeeducli.parsers.resource.hive_metastore_config_parser import HiveMetastoreConfigParser
from yeeducli.parsers.cluster.cluster_conf_parser import ClusterConfigurationParser
from yeeducli.parsers.cluster.cluster_inst_parser import ClusterInstanceParser
from yeeducli.parsers.resource.lookup_parser import LookupParser
from yeeducli.parsers.cluster.download_cluster_instance_log_parser import DownloadClusterInstanceLogParser
from yeeducli.parsers.cluster.cluster_workspace_mapping_parser import ClusterWorkspaceMappingParser
from yeeducli.parsers.workspace.workspace_parser import WorkspaceParser
from yeeducli.parsers.workspace.workspace_files_parser import WorkspaceFilesParser
from yeeducli.parsers.workspace.workspace_access_control_parser import WorkspaceAccessControlParser
from yeeducli.parsers.job.spark_job_config_parser import SparkJobConfigurationParser
from yeeducli.parsers.job.spark_job_parser import SparkJobInstanceParser
from yeeducli.parsers.job.download_job_instance_log_parser import DownloadJobInstanceLogParser
from yeeducli.parsers.notebook.notebook_config_parser import NotebookConfigurationParser
from yeeducli.parsers.notebook.notebook_instance_parser import NotebookInstanceParser
from yeeducli.parsers.notebook.download_notebook_instance_log_parser import DownloadNotebookInstanceLogParser
from yeeducli.parsers.billing.billing_parser import BillingParser
from yeeducli.parsers.iam.user_parser import UserParser
from yeeducli.parsers.iam.shared_platform_and_admin_parser import SharedPlatformAndAdminParser
from yeeducli.parsers.iam.common_platform_and_admin_parser import CommonPlatformAndAdminParser
from yeeducli.parsers.iam.iam_lookup_parser import IamLookupParser
from yeeducli.parsers.iam.platform_admin_parser import PlatformAdminParser
from yeeducli.parsers.token.token_parser import TokenParser
from yeeducli.parsers.secret.tenant_secret_parser import TenantSecretParser
from yeeducli.parsers.secret.user_secret_parser import UserSecretParser
from yeeducli.parsers.secret.workspace_secret_parser import WorkspaceSecretParser
from yeeducli.parsers.metastore_catalog.unity_catalog_parser import UnityCatalogParser
from yeeducli.parsers.catalog_explorer.catalog_explorer_parser import CatalogExplorerParser

from yeeducli.utility.logger_utils import Logger
import sys

logger = Logger.get_logger(__name__, True)


class ServiceParser:
    def create_service_parser(service, subparser):
        try:
            # RESOURCE
            if service == 'resource':

                LookupParser.lookup_parser(subparser)

                VolumeConfigurationParser.volume_configuration_parser(
                    subparser)

                NetworkConfigurationParser.network_configuration_parser(
                    subparser)

                BootDiskImageConfigurationParser.boot_disk_image_config_parser(
                    subparser)

                CredentialsConfigurationParser.credentials_config_parser(
                    subparser)

                CloudEnvironmentParser.cloud_environment_parser(subparser)

                ObjectStorageManagerParser.object_storage_manager_parser(
                    subparser)

                ObjectStorageManagerFilesParser.object_storage_manager_files_parser(
                    subparser)

                HiveMetastoreConfigParser.hive_metastore_config_parser(
                    subparser)

            # CLUSTER
            elif service == 'cluster':

                ClusterConfigurationParser.cluster_configuration_parser(
                    subparser)

                ClusterInstanceParser.cluster_instance_parser(subparser)

                DownloadClusterInstanceLogParser.download_cluster_instance_log_parser(
                    subparser)

                ClusterWorkspaceMappingParser.cluster_workspace_mapping_parser(
                    subparser)

            # WORKSPACE
            elif service == 'workspace':
                WorkspaceParser.workspace_parser(subparser)

                WorkspaceFilesParser.workspace_files_parser(subparser)

                WorkspaceAccessControlParser.workspace_access_control_parser(
                    subparser)

            # JOB
            elif service == 'job':

                SparkJobConfigurationParser.spark_job_configuration_parser(
                    subparser)

                SparkJobInstanceParser.spark_job_parser(subparser)

                DownloadJobInstanceLogParser.download_job_instance_log_parser(
                    subparser)

            # NOTEBOOK
            elif service == 'notebook':

                NotebookConfigurationParser.notebook_configuration_parser(
                    subparser)

                NotebookInstanceParser.notebook_instance_parser(subparser)

                DownloadNotebookInstanceLogParser.download_notebook_instance_log_parser(
                    subparser)

            # BILLING
            elif service == 'billing':

                BillingParser.billing_parser(
                    subparser)

            # IAM
            elif service == 'iam':
                UserParser.user_parser(subparser)

                SharedPlatformAndAdminParser.shared_platform_and_admin_parser(
                    subparser)

                IamLookupParser.iam_lookup_parser(subparser)

            # ADMIN
            elif service == 'admin':

                CommonPlatformAndAdminParser.admin_parser(subparser)

            # PLATFORM ADMIN
            elif service == 'platform-admin':
                PlatformAdminParser.tenant_parser(subparser)

                PlatformAdminParser.platform_admin_parser(subparser)

                CommonPlatformAndAdminParser.platform_admin_parser(subparser)

            # TOKEN
            elif service == 'token':
                TokenParser.token_parser(subparser)

            # SECRET
            elif service == 'secret':
                WorkspaceSecretParser.workspace_secret_parser(subparser)

                TenantSecretParser.tenant_secret_parser(subparser)

                UserSecretParser.user_secret_parser(subparser)

            # METASTORE CATALOG
            elif service == 'metastore-catalog':
                
                MetastoreCatalogParser.metastore_catalog_parser(subparser)
                
                MetastoreTenantSecretParser.tenant_secret_parser(subparser)

                MetastoreUserSecretParser.user_secret_parser(subparser)

                MetastoreWorkspaceSecretParser.workspace_secret_parser(subparser)

            # CATALOG EXPLORER
            elif service == 'catalog-explorer':

                CatalogExplorerParser.catalog_explorer_parser(subparser)

        except Exception as e:
            logger.error(e)
            sys.exit(-1)
