# Generated by Django 5.0.1 on 2024-01-31 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_rename_name_invoice_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='provider',
            field=models.CharField(default='', max_length=50),
        ),
    ]
