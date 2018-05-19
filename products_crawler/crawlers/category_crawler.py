import random
import re

from products_crawler.crawlers.proxies import PROXY_LIST
from products_crawler.crawlers.base_crawler import BaseCrawler


class CategoryCrawler(BaseCrawler):
    
    
    def __init__(self,category_url,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        proxy = random.choice(PROXY_LIST)
        print(':::PROXY:::')
        print(proxy)
        print(':::PROXY:::')
        
        self.r.proxies = {
            'http' : 'http://'+proxy,
            'https': 'https://'+proxy
        }
        self.category_url = category_url
        
        
    def _crawl_now(self):
        
        reps = self._get(self.category_url)
        
        print(reps.request.headers)
        print(reps.request.url)
        
        # f = open('ali.html','w')
        # f.write(reps.text)
        # f.close()
        tree = self.parser(reps.text)

        products = self._extract_products(tree)
        return products
    
    def _extract_products(self,tree):
        
        products = []
        nodes = tree.select('#list-items li')
        if not nodes:
            nodes = tree.select('#hs-list-items li')
        for node in nodes:
            # print(node)
            try:
                id          = node.select_one('input.atc-product-id')
                if not id:
                    id = node.select_one('[data-product-id]').get('data-product-id')
                else:
                    id = id.get('value')
                id          = id.strip()

                url         = node.select_one('a.product')['href']
                name        = node.select_one('a.product').getText().strip()
                image_url   = node.select_one('img.picCore')
                image_url   = image_url.get('image-src',image_url.get('src',''))
                price       = node.select_one('[itemprop="price"]').getText().replace('US $','').split('-')[0]
                order_count = node.select_one('em').getText()
                order_count = re.findall('\((.*?)\)',order_count)[0]
                store       = node.select_one('.store').getText().strip()
                store_url   = node.select_one('a.store').get('href')
                
                if int(order_count) < 5:
                    continue
            except Exception as e:
                print('Error: %s'%e)
                # traceback.print_tb(e.__traceback__)
                # sys.exc_info()
                continue
                
            p = {
                'product_id'    :id,
                'name'          :name,
                'url'           :url,
                'image_url'     :image_url,
                'price'         :price,
                'order_count'   :order_count,
                'store_name'    :store,
                'store_url'     :store_url,
            }
            # print(p)
            products.append(p)
        
        return products