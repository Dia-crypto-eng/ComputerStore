from django.db import models

# Create your models here.
class Category(models.TextChoices):
    KASHABIA='kashabia'    
    THAWB='thawb'

class Product(models.Model):
    
    __name__="product"
    name = models.CharField(max_length=50,default="",blank=False)
    #caractristic = models.CharField(max_length=50,default="",blank=False)
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    brand = models.CharField(max_length=50,default="",blank=False)
    category = models.CharField(max_length=50,choices=Category.choices,default=Category.THAWB)
    stock=models.IntegerField(default=0)
    
    def __str__(self):
        return 

    def __unicode__(self):
        return 
