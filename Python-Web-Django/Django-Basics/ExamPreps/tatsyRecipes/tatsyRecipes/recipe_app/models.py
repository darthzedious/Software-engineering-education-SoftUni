from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from tatsyRecipes.profile_app.models import Profile
from tatsyRecipes.recipe_app.choices import CuisineChoices


class Recipe(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_recipe_title',
                                    violation_error_message="We already have a recipe with the same title!")
        ]
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
        validators=[
            MinLengthValidator(10),
        ],
    )

    cuisine_type = models.CharField(
        null=False,
        blank=False,
        max_length=7,
        choices=CuisineChoices.choices,
    )

    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text="Ingredients must be separated by a comma and space.",
    )

    instructions = models.TextField(
        null=False,
        blank=False,
    )

    cooking_time = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        help_text="Provide the cooking time in minutes.",
        validators=[
            MinValueValidator(1),
        ]
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='recipes',
    )
# 	This field should remain hidden in forms.
