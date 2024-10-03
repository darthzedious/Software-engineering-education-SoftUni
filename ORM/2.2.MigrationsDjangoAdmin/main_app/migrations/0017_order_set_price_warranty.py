# Generated by Django 5.0.4 on 2024-06-29 02:12

from django.db import migrations
from django.utils import timezone


def update_warranty_and_delivery(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')
    orders = order_model.objects.all()

    for order in orders:
        if order.status == 'Pending':
            order.delivery = order.order_date + timezone.timedelta(days=3)
            order.save()
        elif order.status == 'Completed':
            order.warranty = '24 months'
            order.save()
        elif order.status == 'Canceled':
            order.delete()

    #order_model.objects.bulk_update(orders, ['delivery', 'warranty'])


def reverse_default_warranty_and_price(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')
    orders = order_model.objects.all()

    for order in orders:
        if order.status == 'Pending':
            order.delivery = None
        elif order.status == 'Completed':
            order.warranty = order_model._meta.get_field('warranty').default

        order.save()
    # order_model.objects.bulk_update(orders, ['delivery', 'warranty'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_order'),
    ]

    operations = [
        migrations.RunPython(update_warranty_and_delivery, reverse_default_warranty_and_price)
    ]