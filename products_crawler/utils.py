from datetime import datetime, timezone, timedelta
from urllib.parse import quote_plus

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.timezone import now


def back(request,url_name=None,**kwargs):
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/' ))



def parse_cookie_str(str):
    _c = str.split('; ')
    cookies = {}
    for c in _c:
        part = c.split('=')
        cookies[part[0]] = part[1]
    return cookies

def get_aliexpress_category_name(url):
    
    name = url.split('/')[-1].replace('.html','')
    name = name.replace('-',' ').title()
    return name

def _paginator(items,item_per_page=10,page=1):
    paginator = Paginator(items, item_per_page)
    try:
        _items = paginator.page(page)
    except PageNotAnInteger:
        _items = paginator.page(1)
    except EmptyPage:
        _items = paginator.page(paginator.num_pages)
    return _items

def prepare_cate_keyword_url(cate,page):
    time_param = now().strftime('%Y%m%d%H%M%S')
    url = 'https://www.aliexpress.com/wholesale?catId=0&initiative_id=AS_%s&SearchText=%s' % (time_param, quote_plus(cate.keyword))
    return url

def prepare_cate_url(cate,page):
    url = cate.url
    url = url.replace('.html', '/%s.html' % str(page + 1)) if page > 0 else url
    return url

def search_lucky_buyer(buyers):
    _buyers = buyers
    time_dict = {}
    for buyer in _buyers:
        
        if buyer['buyer_name'] in time_dict:
        
            time_dict[buyer['buyer_name']].append(buyer['buyer_time'])
        
        else:
        
            time_dict[buyer['buyer_name']] = [buyer['buyer_time']]
        
        if len(time_dict[buyer['buyer_name']]) >= 5:
            
            time_list = sorted(time_dict[buyer['buyer_name']],reverse=True)
            
            if time_list[0] - time_list[4] <= timedelta(hours=1):
                return buyer['buyer_name']
            
    return None
