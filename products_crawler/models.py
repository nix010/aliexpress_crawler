from django.db import models


class BaseModel(models.Model):

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
        
class Product(BaseModel):
    
    name        = models.CharField(max_length=500)
    url         = models.CharField(max_length=1000)
    image_url   = models.CharField(max_length=1000)
    price       = models.FloatField(default=.0)
    order_count = models.PositiveIntegerField(0)


class Transaction(BaseModel):

    product             = models.ForeignKey(Product,on_delete=models.CASCADE)
    transaction_id      = models.CharField(max_length=500)
    transaction_name    = models.CharField(max_length=500)
    transaction_time    = models.DateTimeField()


