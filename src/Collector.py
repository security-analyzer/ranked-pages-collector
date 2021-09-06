# -*- coding: utf-8 -*-
import re

from url_normalize.tools import unquote
from src.ApiProxy import ApiProxy
from bs4 import BeautifulSoup
from url_normalize import url_normalize

GOOGLE_SEARCH_ENDPOINT = 'https://www.google.com/search?q=site:'


class Collector:

    def __init__(self):
        self._website = ''
        self._per_page = 100
        self._current_page = 0
        self._max_page = 5
        self._suggested_pages = []


    def _get_current_page_url(self):
        return GOOGLE_SEARCH_ENDPOINT + self._website + '&num=' + str(self._per_page) + '&start=' + str(self._per_page * self._current_page)


    def set_current_page(self, current_page):
        self._current_page = current_page


    def set_website(self, website):
        self._website = website


    def set_max_pages(self, max_pages):
        self._max_pages = max_pages


    def set_per_page(self, per_page):
        self._per_page = per_page


    def _next_page(self):
        self._current_page = self._current_page + 1


    def get_suggested_pages(self):
        return self._suggested_pages


    def _normalize_url(self, link):
        try:
            link = url_normalize(link)
            link = unquote(link).decode('utf8')
            return link.strip('/')
        except:
            return link.strip('/')


    def _filter_link(self, link):
        url = self._normalize_url(link)
        if (not url.endswith('.pdf') and 
            not url.endswith('.docx') and 
            not url.endswith('.csv') and 
            not url.endswith('.xlsx')):
            return url
        return False


    def _google_search(self, url):
        api_proxy = ApiProxy()
        html = api_proxy.get_page_html(url)
        if not html:
            return False
        return BeautifulSoup(html, 'html.parser')


    def handle(self):
        for i in range(self._max_page):
            url = self._get_current_page_url()
            google_response = self._google_search(url)
            if google_response:
                soup_links = google_response.select('div.yuRUbf > a')
                if soup_links:
                    for soup_link in soup_links:
                        link_href = soup_link.get('href')
                        filtered_link = self._filter_link(link_href)
                        if filtered_link:
                            self._suggested_pages.append(filtered_link) if filtered_link not in self._suggested_pages else self._suggested_pages
                else:
                    soup_links = google_response.find_all("a")
                    for soup_link in soup_links:
                        link_href = soup_link.get('href')
                        if link_href and "&sa=U&url=" in link_href and not "webcache" in link_href:
                            try:
                                link = link_href.split("&sa=U&url=")[1].split('&ved=')[0]
                                filtered_link = self._filter_link(link)
                                self._suggested_pages.append(filtered_link) if filtered_link not in self._suggested_pages else self._suggested_pages
                            except:
                                continue

            self._next_page()