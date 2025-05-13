from django.db import models

from product.models import Product


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)  # يمكنك إضافة id إذا أردت
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=255, blank=True, null=True)
    minimum_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"
