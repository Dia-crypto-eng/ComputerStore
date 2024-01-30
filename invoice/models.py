from django.db import models as db

# Create your models here.
class Invoice(db.Model):
    
    __name__="invoice"
    date = db.DateField(blank=False)
    amount = db.DecimalField(max_digits=7, decimal_places=2,default=0)
    #caractristic = models.CharField(max_length=50,default="",blank=False)
    def __str__(self):
        return str(self.amount)