from django.db import models as db


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
    PaymentMethod = db.CharField(max_length=20,choices=PAYMENT_CHOICES,default='cash')
    AmountPaid = db.FloatField(default=0)
    PaymentDate= db.DateField(default=0)
    def __str__(self):
        return str(self.AmountPaid)





