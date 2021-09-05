# -*- coding: utf-8 -*-
import re
from src.ApiProxy import ApiProxy
from bs4 import BeautifulSoup
from url_normalize import url_normalize

GOOGLE_SEARCH_ENDPOINT = 'https://www.google.com/search?num=1008&q=site:'


class Collector:

    def __init__(self):
        self._website = ''
        self._suggested_pages = []


    def set_website(self, website):
        self._website = website


    def get_suggested_pages(self):
        return self._suggested_pages


    def _normalize_url(self, link):
        try:
            url = re.search(r'url\?q=(.*?)&sa=', link).group(1)
        except:
            url = link
        return url_normalize(url)


    def _filter_link(self, link):
        url = self._normalize_url(link)
        if (not url.endswith('.pdf') and 
            not url.endswith('.docx') and 
            not url.endswith('.csv') and 
            not url.endswith('.xlsx')):
            return url
        return False


    def _google_search(self):
        url = GOOGLE_SEARCH_ENDPOINT + self._website
        api_proxy = ApiProxy()
        html = api_proxy.get_page_html(url)
        if not html:
            return False
        return BeautifulSoup(html, 'html.parser')


    def handle(self):
        google_response = self._google_search()
        if google_response:
            soup_links = google_response.select('div.yuRUbf > a')
            if soup_links:
                for soup_link in soup_links:
                    link_href = soup_link.get('href')
                    filtred_link = self._filter_link(link_href)
                    if filtred_link:
                        self._suggested_pages.append(filtred_link)
            else:
                soup_links = google_response.find_all("a")
                for soup_link in soup_links:
                    link_href = soup_link.get('href')
                    if link_href and "&sa=U&url=" in link_href and not "webcache" in link_href:
                        try:
                            link = link_href.split("&sa=U&url=")[1].split('&ved=')[0]
                            filtred_link = self._filter_link(link)
                            self._suggested_pages.append(filtred_link)
                        except:
                            continue