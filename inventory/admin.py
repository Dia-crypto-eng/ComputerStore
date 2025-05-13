from django.contrib import admin

# Register your models here.
from inventory.models import Inventory

admin.site.register(Inventory)