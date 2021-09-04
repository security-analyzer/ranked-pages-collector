# -*- coding: utf-8 -*-
import requests

SCRAPER_API_KEY = 'c7812d010f0872133f1fe79b833455fb'
SCRAPER_API_ENDPOINT = 'http://api.scraperapi.com?api_key=' + SCRAPER_API_KEY + '&url='


class ApiProxy:

    def get_page_html(self, url):
        try:
            response = requests.get(SCRAPER_API_ENDPOINT + url)
            return response.content
        except:
            return False
