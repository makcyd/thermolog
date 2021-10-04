import requests
import logging

from django.conf import settings

logger = logging.getLogger(__name__)


def get_current():
    url = "https://api.weatherapi.com/v1/current.json"
    logger.info("Calling Weather API. URL: {}, PARAMS: {}".format(url, settings.WEATHERAPI_PARAMS))
    response = requests.get(url, params=settings.WEATHERAPI_PARAMS)
    if response.status_code in [200]:
        logger.info("Success! Response: {}".format(response.json()))
        return response.json()
    else:
        logger.error("Error: {}".format(response.text))
        return None
