from yeeducli.utility.json_utils import response_validator
from yeeducli.utility.request_utils import Requests
from yeeducli.utility.logger_utils import Logger
from yeeducli import config
import requests
import sys

logger = Logger.get_logger(__name__, True)


class CloudEnvironment:

    def add_cloud_env(json_data):
        try:
            url = f"{config.YEEDU_RESTAPI_URL}/cluster/cloud/environment"

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

    def list_cloud_env(page_number, limit, cloud_provider=None, architecture_type=None):
        try:
            url = f"{config.YEEDU_RESTAPI_URL}/cluster/cloud/environments"

            response = Requests(
                url=url,
                method="GET",
                headers=config.headers,
                params={
                    "cloud_provider": cloud_provider,
                    "architecture_type": architecture_type,
                    "pageNumber": page_number,
                    "limit": limit
                }
            ).send_http_request()

            return response_validator(response)
        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)

    def search_cloud_env(cloud_env_name, page_number, limit, cloud_provider=None, architecture_type=None):
        try:
            url = f"{config.YEEDU_RESTAPI_URL}/cluster/cloud/environments/search"

            response = Requests(
                url=url,
                method="GET",
                headers=config.headers,
                params={
                    "cloud_env_name": cloud_env_name,
                    "cloud_provider": cloud_provider,
                    "architecture_type": architecture_type,
                    "pageNumber": page_number,
                    "limit": limit
                }
            ).send_http_request()

            return response_validator(response)
        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)

    def get_cloud_env(cloud_env_id=None, cloud_env_name=None):
        try:
            url = f'{config.YEEDU_RESTAPI_URL}/cluster/cloud/environment'

            response = Requests(
                url=url,
                method="GET",
                headers=config.headers,
                params={
                    "cloud_env_id": cloud_env_id,
                    "cloud_env_name": cloud_env_name
                }
            ).send_http_request()

            return response_validator(response)
        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)

    def edit_cloud_env(json_data, cloud_env_id=None, cloud_env_name=None):
        try:
            url = f'{config.YEEDU_RESTAPI_URL}/cluster/cloud/environment'

            response = Requests(
                url=url,
                method="PUT",
                headers=config.headers,
                data=json_data,
                params={
                    "cloud_env_id": cloud_env_id,
                    "cloud_env_name": cloud_env_name
                }
            ).send_http_request()

            return response_validator(response)
        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)

    def delete_cloud_env(cloud_env_id=None, cloud_env_name=None):
        try:
            url = f'{config.YEEDU_RESTAPI_URL}/cluster/cloud/environment'

            response = Requests(
                url=url,
                method="DELETE",
                headers=config.headers,
                params={
                    "cloud_env_id": cloud_env_id,
                    "cloud_env_name": cloud_env_name
                }
            ).send_http_request()

            return response_validator(response)
        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)
