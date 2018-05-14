import re
from products_crawler.crawlers.base_crawler import BaseCrawler


class CategoryCrawler(BaseCrawler):
    
    
    def __init__(self,category_url,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.category_url = category_url
        
        
        
    def _crawl_now(self):
        
        reps = self._get(self.category_url)
        tree = self.parser(reps.text)

        products = self._extract_products(tree)
        
        return products
    
    def _extract_products(self,tree):
        
        products = []
        for node in tree.select('#list-items .item'):
            
            try:
                id          = node.select_one('a.atc-product-id').get('value').strip()
                url         = node.select_one('a.product')['href']
                name        = node.select_one('a.product').getText().strip()
                image_url   = node.select_one('img.picCore').get('image-src')
                price       = node.select_one('[itemprop="price"]').getText().replace('US $','').split('-')[0]
                order_count = re.findall('Orders \((.*?)\)',node.select_one('em').getText())[0]
                store       = node.select_one('.store-name').getText().strip()
                store_url   = node.select_one('.store-name a').get('href')
            except:
                continue
                
            p = {
                'id'            :id,
                'name'          :name,
                'url'           :url,
                'image_url'     :image_url,
                'price'         :price,
                'order_count'   :order_count,
                'store'         :store,
                'store_url'     :store_url,
            }
            products.append(p)
        
        return products