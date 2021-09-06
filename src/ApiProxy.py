# -*- coding: utf-8 -*-
from src.Utils import config
import requests

ERROR_MESSAGE = 'Request failed. You will not be charged for this request'

class ApiProxy:

    def get_page_html(self, url):
        configs = config('scraperapi')
        scraper_api_endpoint = configs['scraper_api_endpoint'] + '?api_key=' + configs['scraper_api_key'] + '&url=' + url
        retry_count = config('api_proxy')['retry_count']
        try:
            retry = 0
            response = requests.get(scraper_api_endpoint)
            while retry <= retry_count and ERROR_MESSAGE in response.text:
                response = requests.get(scraper_api_endpoint)
                retry = retry + 1
            return response.text
        except:
            return False
