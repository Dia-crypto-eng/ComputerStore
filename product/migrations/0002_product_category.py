# Generated by Django 5.0.1 on 2024-01-07 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('kashabia', 'Kashabia'), ('thawb', 'Thawb')], default='thawb', max_length=50),
        ),
    ]
