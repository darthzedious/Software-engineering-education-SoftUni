# Generated by Django 5.1.2 on 2024-10-24 17:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AddConstraint(
            model_name='recipe',
            constraint=models.UniqueConstraint(fields=('title',), name='unique_recipe_title', violation_error_message='We already have a recipe with the same title!'),
        ),
    ]