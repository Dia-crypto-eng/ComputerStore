from django.contrib import admin

from invoice.models import BuyInvoice,InvoiceItem,SellInvoice

# Register your models here.
admin.site.register(BuyInvoice)
admin.site.register(InvoiceItem)
admin.site.register(SellInvoice)