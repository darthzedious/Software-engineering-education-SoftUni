# Generated by Django 5.0.4 on 2024-06-28 20:16

from django.db import migrations


def set_rarity(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')

    items = item_model.objects.all()

    for item in items:
        if item.price <= 10:
            item.rarity = 'Rare'
        elif item.price <= 20:
            item.rarity = "Very Rare"
        elif item.price <= 30:
            item.rarity = "Extremely Rare"
        else:
            item.rarity = "Mega Rare"

    item_model.objects.bulk_update(items, ['rarity'])


def set_rarity_default(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')

    items = item_model.objects.all()

    for item in items:
        item.rarity = item_model._meta.get_field('rarity').default
        #person.save()

    item_model.objects.bulk_update(items, ['rarity'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_item'),
    ]

    operations = [
        migrations.RunPython(set_rarity, set_rarity_default)
    ]
