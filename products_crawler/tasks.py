from datetime import timedelta
import time
from project.celery import app

# app.conf.beat_schedule = {
    # 'update_shopify_site_schedule': {
    #     'task': 'shopify_sites.tasks.update_shopify_site',
    #     'schedule': 2*60*60,
    # },
# }

@app.task
def crawl_category(cate_id):
    
    from products_crawler.models import Product,Category,AliexpressCookie

    from products_crawler.crawlers.category_crawler import CategoryCrawler

    cate    = Category.objects.get(id=cate_id)
    
    page_num = 10
    for p in range(page_num):
        if p > 0:
            url = cate.url.replace('.html', '/%s.html' % str(p+1))
        else:
            time.sleep(7)
            url = cate.url
        print(url)
        cookie  = AliexpressCookie.objects.filter(state=AliexpressCookie.STATE_OK).first()
        if not cookie:
            return 'No-Cookie'

        res     = CategoryCrawler(url,cookies=cookie.cookies).crawl_now()
        
        if res.get('cookies'):
            cookie.cookies = res.get('cookies')
            cookie.save()
    
        products = res['data']
        print('Got %d item(s)'%len(products))
        for product in products:
            product.update({
                'category':cate
            })
    
            _product,_ = Product.objects.update_or_create(
                product_id  = product['product_id'],
                defaults    = product
            )
            crawl_product_buyer.delay(prod_id=_product.id)
    
    
@app.task
def crawl_product_buyer(prod_id=None):
    
    from products_crawler.models import Product,Buyer,AliexpressCookie
    from products_crawler.crawlers.transaction_crawler import TransactionCrawler
    from products_crawler.utils import search_lucky_buyer

    # cookie  = AliexpressCookie.objects.filter(state=AliexpressCookie.STATE_OK).first()
    product = Product.objects.get(id=prod_id)
    
    for i in range(1,11):
        res     = TransactionCrawler(
            trans_id    = product.product_id,
            page        = i,
            # cookies     = cookie.cookies,
        ).crawl_now()
        
        buyers  = res['data']

        lucky_buyer = search_lucky_buyer(buyers)
        
        

        for buyer in buyers:
            buyer.update({
                'product'       : product,
                'buyer_lucky'   : buyer['buyer_name'] == lucky_buyer,
            })
            _buyer,_ = Buyer.objects.update_or_create(
                product     = buyer['product'],
                buyer_name  = buyer['buyer_name'],
                buyer_time  = buyer['buyer_time'],
                defaults    = buyer
            )
        
        