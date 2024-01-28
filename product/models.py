from django.db import models as db

# Create your models here.









class Category(db.TextChoices):
    LAPTOP='laptop'    
    RAM='ram'

class Product(db.Model):
    
    __name__="product"
    name = db.CharField(max_length=50,default="more",blank=True)
    #caractristic = models.CharField(max_length=50,default="",blank=False)
    price = db.DecimalField(max_digits=7,decimal_places=2,default=0)
    brand = db.CharField(max_length=50,default="",blank=False)
    category = db.CharField(max_length=50,choices=Category.choices,default=Category.LAPTOP)
    stock=db.IntegerField(default=0)
    
    def __str__(self):
        return 

    def __unicode__(self):
        return 
