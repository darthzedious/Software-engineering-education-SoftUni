# Generated by Django 5.0.4 on 2024-06-29 00:57

from django.db import migrations


def set_price(apps, schema_editor):
    MULTIPLIER = 120
    phone_model = apps.get_model('main_app', 'Smartphone')

    phones = phone_model.objects.all()

    for phone in phones:
        phone.price = MULTIPLIER * len(phone.brand)

    phone_model.objects.bulk_update(phones, ['price'])


def set_category(apps, schema_editor):
    phone_model = apps.get_model('main_app', 'Smartphone')
    phones = phone_model.objects.all()

    for phone in phones:
        if phone.price >= 750:
            phone.category = 'Expensive'
        else:
            phone.category = 'Cheap'

    phone_model.objects.bulk_update(phones, ['category'])


def set_all_columns(apps, schema_editor):
    set_price(apps, schema_editor)
    set_category(apps, schema_editor)


def reverse_price_category(apps, schema_editor):
    phone_model = apps.get_model('main_app', 'Smartphone')
    phones = phone_model.objects.all()

    for phone in phones:
        phone.category = phone_model._meta.get_field('category').default
        phone.price = phone_model._meta.get_field('price').default

    phone_model.objects.bulk_update(phones, ['category', 'price'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_smartphone'),
    ]

    operations = [
        migrations.RunPython(set_all_columns, reverse_price_category)
    ]
