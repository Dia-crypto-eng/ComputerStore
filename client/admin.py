from django.contrib import admin
from client.models import Client, Company, ClientCompanyLink ,PaymentInvoiceLink, Payment
# Register your models here.
 
admin.site.register(ClientCompanyLink)
admin.site.register(Client)
admin.site.register(Company)
admin.site.register(PaymentInvoiceLink)
admin.site.register(Payment)
