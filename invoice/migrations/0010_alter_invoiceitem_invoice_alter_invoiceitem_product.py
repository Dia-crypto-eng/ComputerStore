# Generated by Django 5.0.1 on 2024-04-11 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_alter_invoiceitem_price_buy'),
        ('product', '0010_remove_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice.invoice'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product'),
        ),
    ]
