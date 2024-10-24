from django.core.validators import MinLengthValidator
from django.db import models

from tatsyRecipes.utils.validators import CapitalFirstLetterValidator


class Profile(models.Model):
    nickname = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=20,
        validators=[
            MinLengthValidator(2, message="Nickname must be at least 2 chars long!"),
        ],
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=[
            CapitalFirstLetterValidator(),
        ],
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=[
            CapitalFirstLetterValidator(),
        ],
    )

    chef = models.BooleanField(
        blank=False,
        default=False,
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )

