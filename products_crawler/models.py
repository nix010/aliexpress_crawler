from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import Count, Q
from urllib.parse import urlparse,parse_qs


class BaseModel(models.Model):

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return getattr(self,'name',super().__str__())

    class Meta:
        abstract = True
        
        
class AliexpressCookie(BaseModel):
    
    STATE_OK    = 'ok'
    STATE_ERROR = 'damaged'
    STATE_USING = 'using'
    
    cookies     = JSONField()
    state       = models.CharField(max_length=50,default=STATE_OK)
    
    def __str__(self):
        return ('<%s> - %s'%(str(self.cookies)[:30],self.updated_at))
    
    
    
class Category(BaseModel):
    
    name        = models.CharField(max_length=500)
    url         = models.CharField(max_length=1000)
    keyword     = models.CharField(max_length=100,blank=True,null=True)

    def is_keyword(self):
        return bool(self.keyword)
    
    def valid_product_set(self):
        return self.product_set.all().annotate(lucky = Count('buyer', filter = Q(buyer__buyer_lucky=True)) )\
            .filter(lucky__gte =1)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        
        self.url = 'https:' + self.url if self.url and self.url.startswith("//") else self.url
        self.url = self.url.split('?')[0]

        super().save(force_insert=False, force_update=False, using=None, update_fields=None)
    
    
class Product(BaseModel):
    
    product_id  = models.CharField(max_length=500)
    name        = models.CharField(max_length=500)
    url         = models.CharField(max_length=1000)
    image_url   = models.CharField(max_length=1000)
    store_name  = models.CharField(max_length=1000)
    store_url   = models.CharField(max_length=1000)
    price       = models.FloatField(default=.0)
    order_count = models.PositiveIntegerField(0)
    category    = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        
        self.url        = 'https:'+self.url if self.url and self.url.startswith("//") else self.url
        self.image_url  = 'https:'+self.image_url if self.image_url and self.image_url.startswith("//") else self.image_url
        self.store_url  = 'https:'+self.store_url if self.store_url and self.store_url.startswith("//") else self.store_url
        super().save(force_insert=False, force_update=False, using=None,update_fields=None)
        
        
    def latest_buyer5(self):
        return self.buyer_set.all().filter(buyer_lucky=True).order_by('-buyer_time').first()

class Buyer(BaseModel):

    product     = models.ForeignKey(Product,on_delete=models.CASCADE)
    buyer_name  = models.CharField(max_length=500)
    buyer_time  = models.DateTimeField()
    buyer_lucky = models.BooleanField(default=False)
    
    def __str__(self):
        return ('"%s" - %s'%(str(self.buyer_name),self.buyer_time))



