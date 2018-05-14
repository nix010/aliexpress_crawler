from django.contrib.postgres.fields import JSONField
from django.db import models


class BaseModel(models.Model):

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return getattr(self,'name',super().__str__())

    class Meta:
        abstract = True
        
        
class AliexpressCookie(BaseModel):
    
    cookies     = JSONField()
    
    def __str__(self):
        return ('<%s> - %s'%(str(self.cookies),self.updated_at))
    
class Product(BaseModel):
    
    product_id  = models.CharField(max_length=500)
    name        = models.CharField(max_length=500)
    url         = models.CharField(max_length=1000)
    image_url   = models.CharField(max_length=1000)
    store_name  = models.CharField(max_length=1000)
    store_url   = models.CharField(max_length=1000)
    price       = models.FloatField(default=.0)
    order_count = models.PositiveIntegerField(0)
    
    def latest_buyer5(self):
        return self.buyer_set.all().values('buyer_name').order_by('-buyer_time').first()


class Buyer(BaseModel):

    product     = models.ForeignKey(Product,on_delete=models.CASCADE)
    # buyer_id    = models.CharField(max_length=500)
    buyer_name  = models.CharField(max_length=500)
    buyer_time  = models.DateTimeField()
    
    def __str__(self):
        return ('"%s" - %s'%(str(self.buyer_name),self.buyer_time))



