from utils.logger import logger
import json


class APILogger:

    @staticmethod
    def log_request(method, url, payload=None, params=None):

        logger.info("\n--- API REQUEST ---")
        logger.info(f"Method: {method}")
        logger.info(f"URL: {url}")

        if payload:
            logger.info(f"Payload:\n{json.dumps(payload, indent=2)}")

        if params:
            logger.info(f"Params: {params}")

    @staticmethod
    def log_response(response):

        logger.info("\n--- API RESPONSE ---")
        logger.info(f"Status Code: {response.status_code}")

        try:
            body = response.json()
            logger.info(f"Response Body:\n{json.dumps(body, indent=2)}")
        except Exception:
            logger.info(f"Response Text:\n{response.text}")