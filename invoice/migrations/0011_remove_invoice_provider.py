# Generated by Django 5.0.1 on 2024-08-26 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0010_alter_invoiceitem_invoice_alter_invoiceitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='provider',
        ),
    ]
