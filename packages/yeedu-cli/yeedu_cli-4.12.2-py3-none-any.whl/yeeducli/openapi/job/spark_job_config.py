from yeeducli.utility.file_utils import FileUtils
from yeeducli.utility.json_utils import response_validator
from yeeducli.utility.request_utils import Requests
from yeeducli.utility.logger_utils import Logger
from yeeducli import config
import requests
import sys

logger = Logger.get_logger(__name__, True)


class SparkJobConfig:
    def list_spark_job_config(workspace_id, enable, pageNumber, limit, cluster_ids=None, job_type=None, job_type_langs=None, has_run=None, last_run_status=None, created_by_ids=None, modified_by_ids=None):
        try:
            url = f"{config.YEEDU_RESTAPI_URL}/workspace/{workspace_id}/spark/jobs"

            response = Requests(
                url=url,
                method="GET",
                headers=config.headers,
                params={
                    "enable": enable,
                    "cluster_ids": cluster_ids,
                    "job_type": job_type,
                    "job_type_langs": job_type_langs,
                    "last_run_status": [status.upper() for status in last_run_status] if isinstance(last_run_status, list) else None,
                    "has_run": has_run,
                    "created_by_ids": created_by_ids,
                    "modified_by_ids": modified_by_ids,
                    "pageNumber": pageNumber,
                    "limit": limit
                }
            ).send_http_request()

            return response_validator(response)
        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)

    def search_spark_job_config_by_workspaceId_and_name(workspace_id, job_name, enable, pageNumber, limit, cluster_ids=None, job_type=None, job_type_langs=None, has_run=None, last_run_status=None, created_by_ids=None, modified_by_ids=None):
        try:
            url = f"{config.YEEDU_RESTAPI_URL}/workspace/{workspace_id}/spark/jobs/search"

            response = Requests(
                url=url,
                method="GET",
                headers=config.headers,
                params={
                    "job_name": job_name,
                    "enable": enable,
                    "cluster_ids": cluster_ids,
                    "job_type": job_type,
                    "job_type_langs": job_type_langs,
                    "has_run": has_run,
                    "last_run_status": [status.upper() for status in last_run_status] if isinstance(last_run_status, list) else None,
                    "created_by_ids": created_by_ids,
                    "modified_by_ids": modified_by_ids,
                    "pageNumber": pageNumber,
                    "limit": limit
                }
            ).send_http_request()

            return response_validator(response)
        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)

    def add_spark_job_config(workspace_id, json_data):
        try:
            url = f"{config.YEEDU_RESTAPI_URL}/workspace/{workspace_id}/spark/job"

            response = Requests(
                url=url,
                method="POST",
                headers=config.headers,
                json=json_data
            ).send_http_request()

            return response_validator(response)
        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)

    def get_spark_job_config_by_id_or_name(workspace_id, job_id=None, job_name=None):
        try:
            url = f"{config.YEEDU_RESTAPI_URL}/workspace/{workspace_id}/spark/job"

            response = Requests(
                url=url,
                method="GET",
                headers=config.headers,
                params={
                    "job_name": job_name,
                    "job_id": job_id
                }
            ).send_http_request()

            return response_validator(response)
        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)

    def edit_spark_job_config(workspace_id, json_data, job_id=None, job_name=None):
        try:
            url = f"{config.YEEDU_RESTAPI_URL}/workspace/{workspace_id}/spark/job"

            response = Requests(
                url=url,
                method="PUT",
                headers=config.headers,
                data=json_data,
                params={
                    "job_name": job_name,
                    "job_id": job_id
                }
            ).send_http_request()

            return response_validator(response)
        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)

    def enable_spark_job_config_by_id_or_name(workspace_id, job_id=None, job_name=None):
        try:
            url = f"{config.YEEDU_RESTAPI_URL}/workspace/{workspace_id}/spark/job/enable"

            response = Requests(
                url=url,
                method="PUT",
                headers=config.headers,
                params={
                    "job_id": job_id,
                    "job_name": job_name
                }
            ).send_http_request()

            return response_validator(response)
        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)

    def disable_spark_job_config_by_id_or_name(workspace_id, job_id=None, job_name=None):
        try:
            url = f"{config.YEEDU_RESTAPI_URL}/workspace/{workspace_id}/spark/job/disable"

            response = Requests(
                url=url,
                method="PUT",
                headers=config.headers,
                params={
                    "job_id": job_id,
                    "job_name": job_name
                }
            ).send_http_request()

            return response_validator(response)
        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)

    def export_spark_job_config(workspace_id, job_id=None, job_name=None):
        try:
            url = f"{config.YEEDU_RESTAPI_URL}/workspace/{workspace_id}/spark/job/export"

            response = Requests(
                url=url,
                method="GET",
                headers=config.headers,
                params={
                    "job_name": job_name,
                    "job_id": job_id
                }
            ).send_http_request()

            return FileUtils.process_file_response(response, save_to_disk=True)

        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)
