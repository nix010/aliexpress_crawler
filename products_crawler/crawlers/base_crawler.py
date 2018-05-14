import json
from bs4 import BeautifulSoup as BS

import requests


class BaseCrawler(object):
    
    default_headers = {
        'Accept'                   : '*/*',
        'Cache-Control'            : 'no-cache',
        'upgrade-insecure-requests': '1',
        'User-Agent'               : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.94 Chrome/62.0.3202.94 Safari/537.36'
    }
    _save_to_db = True
    
    def __init__(self):
        self.r = requests.Session()
    
    
    def crawl_now(self):
        return 'Completed'
    
    def _get(self, url, params=None, headers=None, cookies=None):
        if params is None:
            params = {}
        if cookies is None:
            cookies = {}
        h = self.default_headers
        if headers:
            h.update(headers)
        return self.r.get(url, params=params, headers=h, cookies=cookies, timeout=10)
    
    def _post(self, url, data=None, headers=None):
        h = self.default_headers
        if headers is not None:
            h.update(headers)
        return self.r.post(url, data=data, headers=h, allow_redirects=False, timeout=10)
    
    def load_json_js(self, text):
        return json.loads(text.replace('for (;;);', ''))
    
    def parser(self, html):
        return BS(html, 'html.parser')
    
    def xml_parser(self, xml):
        return BS(xml, 'xml')
    
