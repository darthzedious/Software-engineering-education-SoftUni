# Generated by Django 5.0.4 on 2024-07-21 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_product_discountproducts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DiscountProducts',
        ),
        migrations.CreateModel(
            name='DiscountedProduct',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.product',),
        ),
    ]
