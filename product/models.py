from django.db import models as db

# Create your models here.


class Category(db.Model):
        
    __name__="category"    
    name = db.CharField(max_length=250,unique=True , default="",blank=False)    
    def __str__(self):
        return self.name
    
    
class Product(db.Model):
    
    __name__="product"
    IdProduct=db.AutoField(primary_key=True)
    name = db.CharField(max_length=50,default="more",blank=True)
    #caractristic = models.CharField(max_length=50,default="",blank=False)
    mark = db.CharField(max_length=50,default="",blank=False)
    category = db.ForeignKey(Category,on_delete=db.PROTECT,related_name="products")
    # picture=db.ImageField(upload_to="my_picture",blank=True)
    stock=db.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return 
