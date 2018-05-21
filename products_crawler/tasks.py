import time

from products_crawler.crawlers.category_keyword_crawler import CategoryKeywordCrawler
from products_crawler.utils import prepare_cate_keyword_url
from project.celery import app

app.conf.beat_schedule = {
    'update_aliexpress_category': {
        'task': 'products_crawler.tasks.update_categories',
        'schedule': 60*60,
    },
}


@app.task
def update_categories():
    from products_crawler.models import Category
    from django.db.models import Count
    cates = Category.objects.all().annotate(product_count=Count('product')).order_by('-product_count')
    
    for idx,cate in enumerate(cates):
        crawl_category.delay(cate.id, 20*idx)
    
@app.task
def crawl_keyword_category(cate_id,sleep_time=0):
    print('::KEYWORD')
    crawl_category(cate_id,sleep_time , url_function=prepare_cate_keyword_url, crawler=CategoryKeywordCrawler)
    
    
@app.task
def crawl_category(cate_id,sleep_time=0,url_function=None,crawler=None):
    
    time.sleep(sleep_time)
    
    from products_crawler.models import Product,Category
    from products_crawler.utils import prepare_cate_url
    from products_crawler.crawlers.category_crawler import CategoryCrawler
    
    print('cate_id')
    cate    = Category.objects.get(id=cate_id)

    if not crawler:
        crawler = CategoryCrawler
    if not url_function:
        url_function = prepare_cate_url

    page_num = 10
    for p in range(page_num):
    
        url = url_function(cate,p)
        
        print(url)

        res     = crawler(url).crawl_now()
        
    
        products = res['data']
        if len(products) == 0:
            print('\n================')
            print('End with error ')
            break
            
        print('Got %d item(s)'%len(products))
        
        for product in products:
            
            if not product.get('category'):
                product.update({
                    'category': cate
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
        
        