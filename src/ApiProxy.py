# -*- coding: utf-8 -*-
import requests

SCRAPER_API_KEY = 'c7812d010f0872133f1fe79b833455fb'
SCRAPER_API_ENDPOINT = 'http://api.scraperapi.com?api_key=' + SCRAPER_API_KEY + '&url='
RETRY_COUNT = 3
ERROR_MESSAGE = 'Request failed. You will not be charged for this request'

class ApiProxy:

    def get_page_html(self, url):
        try:
            retry = 0
            response = requests.get(SCRAPER_API_ENDPOINT + url)
            while retry <= RETRY_COUNT and ERROR_MESSAGE in response.text:
                response = requests.get(SCRAPER_API_ENDPOINT + url)
                retry = retry + 1
            return response.text
        except:
            return False
