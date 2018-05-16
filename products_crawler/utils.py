from datetime import datetime, timezone, timedelta

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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

def search_lucky_buyer(buyers):
    _buyers = buyers
    time_dict = {}
    for buyer in _buyers:
        if buyer['buyer_name'] in time_dict:
            time_dict[buyer['buyer_name']].append(buyer['buyer_time'])
        else:
            time_dict[buyer['buyer_name']] = [buyer['buyer_time']]
        
        if len(time_dict[buyer['buyer_name']]) >= 5:
            time_list = sorted(time_dict[buyer['buyer_name']])
            if time_list[0] - time_list[4] <= timedelta(hours=1):
                return buyer['buyer_name']
            
    return False
