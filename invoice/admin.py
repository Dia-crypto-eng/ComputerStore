from django.contrib import admin

from invoice.models import Invoice,InvoiceItem

# Register your models here.
admin.site.register(Invoice)
admin.site.register(InvoiceItem)