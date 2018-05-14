from datetime import datetime, timezone
def back(request,url_name=None,**kwargs):
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/' ))


def now():
    return datetime.now(timezone.utc)

def parse_cookie_str(str):
    _c = str.split('; ')
    cookies = {}
    for c in _c:
        part = c.split('=')
        cookies[part[0]] = part[1]
    return cookies

def get_shopify_site_name(url):
    
    import requests
    resp = requests.get(url)
    from bs4 import BeautifulSoup
    title = BeautifulSoup(resp.text,'html.parser').select_one('title')
    return title.get_text().strip() if title else None
    