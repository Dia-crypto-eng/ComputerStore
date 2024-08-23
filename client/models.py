from django.db import models as db

from invoice.models import Invoice

# Create your models here.


# 1. Clients
# ClientID
# FirstName
# LastName
# Email
# PhoneNumber
# ProfilePicture
# Notes

class Client(db.Model):
    
    __name__="client"
    ClientID=db.AutoField(primary_key=True)
    FirstName=db.CharField(max_length=50,default="",blank=False)
    LastName=db.CharField(max_length=50,default="",blank=False)
    Email = db.EmailField(unique=True)
    PhoneNumber= db.CharField(max_length=10)
    #ProfilePicture=db.ImageField(upload_to="Client",blank=True)
    #Notes = db.TextField(default="",blank=False)
    def __str__(self):
        return str(self.FirstName+self.LastName)


# 2. Companies
# CompanyID
# CompanyName
# CRN
# NIS
# NIF
# Address

class Company(db.Model):
    
    __name__="company"
    CompanyID=db.AutoField(primary_key=True)
    CompanyName=db.CharField(max_length=50,default="",blank=False)
    CRN=db.CharField(max_length=25,default="",blank=False)
    NIS=db.CharField(max_length=25,default="",blank=False)
    NIF=db.CharField(max_length=25,default="",blank=False)
    #Address = db.TextField(default="",blank=False)
    def __str__(self):
        return str(self.CompanyName)


# 3. Payments
# PaymentID
# ClientID
# PaymentMethod
# AmountPaid
# PaymentDate


PAYMENT_CHOICES = [
    ('fundtransfer', 'Fund Transfer'),
    ('check', 'Check'),
    ('cash', 'Cash'), # إضافة طريقة الدفع الجديدة
]

class Payment(db.Model):
    
    __name__="payment"
    PaymentID=db.AutoField(primary_key=True)
    Client = db.ForeignKey(Client,on_delete=db.PROTECT)
    PaymentMethod = db.CharField(max_length=20,choices=PAYMENT_CHOICES,default='cash')
    AmountPaid = db.FloatField(default=0)
    PaymentDate= db.DateField(default=0)
    def __str__(self):
        return str(self.Client.FirstName+self.Client.LastName)


# 4. PaymentInvoiceLinks
# LinkID
# ClientID
# IsPayment
# RelatedID


class PaymentInvoiceLink(db.Model):
    
    LINK_TYPE_CHOICES = [
        ('payment', 'Payment'),
        ('invoice', 'Invoice'),
    ]
    
    __name__="paymentInvoiceLink"
    link_id = db.AutoField(primary_key=True)
    client = db.ForeignKey(Client, on_delete=db.CASCADE)
    is_payment = db.CharField(max_length=10,choices=LINK_TYPE_CHOICES)
    related_payment = db.ForeignKey(Payment, null=True, blank=True, on_delete=db.CASCADE)
    related_invoice = db.ForeignKey(Invoice, null=True, blank=True, on_delete=db.CASCADE)

    def save(self, *args, **kwargs):
        # تحديد الحقول المرتبطة بناءً على قيمة is_payment
        if self.is_payment == 'payment':
            self.related_invoice = None
        elif self.is_payment == 'invoice':
            self.related_payment = None
        super().save(*args, **kwargs)

    def __str__(self):
        if self.is_payment == 'payment':
            return f"Client: {self.client}, Payment ID: {self.related_payment.id}"
        elif self.is_payment == 'invoice':
            return f"Client: {self.client}, Invoice ID: {self.related_invoice.id}"



# 5. ClientCompanyLinks
# LinkID
# ClientID
# CompanyID


class ClientCompanyLink(db.Model):
    
    __name__="clientCompanyLink"
    LinkID=db.AutoField(primary_key=True)
    Client = db.ForeignKey(Client,on_delete=db.PROTECT)
    Company = db.ForeignKey(Company,on_delete=db.PROTECT)
    
    def __str__(self):
        return str(self.Client.FirstName+self.Client.LastName)