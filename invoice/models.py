from django.db import models as db
from product.models import Product
from client.models import ClientCompanyLink
# Create your models here.


class Invoice(db.Model):
    
#     __name__="invoice"
    id=db.AutoField(primary_key=True)
    date = db.DateField(blank=False)
#     #provider=db.CharField(max_length=50,default="",blank=False)
#     #provider=db.ForeignKey(Client,on_delete=db.PROTECT,default=1)
    amount = db.FloatField(default=0)
#     #caractristic = models.CharField(max_length=50,default="",blank=False)
    def __str__(self):
         return str(self.amount)
    class Meta:
        abstract = True

class BuyInvoice(Invoice):
    
    __name__="buy_invoice"
    client = db.ForeignKey(ClientCompanyLink, on_delete=db.CASCADE)
    class Meta:
        db_table = 'invoice_buyinvoice'
    
    def __str__(self):
        return str(self.amount)
     
     
     
Sold= ( ("PAID" , "PAID"), 
                ("UNPAID"  , "UNPAID"))   
class SellInvoice(Invoice):
     
     sold = db.CharField(max_length=10, choices=Sold)  
     class Meta:
         db_table = 'invoice_sellinvoice'  # اسم جديد للجدول
         


class InvoiceItem(db.Model):
    
    __name__="invoiceItem"
    idInvoiceElement=db.AutoField(primary_key=True)
    invoice = db.ForeignKey(BuyInvoice,on_delete=db.PROTECT)
    product=db.ForeignKey(Product,on_delete=db.PROTECT)
    price_buy = db.FloatField(default=0)
    quantity= db.IntegerField(default=0)
    #caractristic = models.CharField(max_length=50,default="",blank=False)
    def __str__(self):
        return str(self.idInvoiceElement)


  