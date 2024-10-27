from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Model

from FurryFunnies.utils.validators import ContainLettersOnlyValidator, validate_passcode


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            ContainLettersOnlyValidator(),
        ],
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            ContainLettersOnlyValidator(),
        ]
    )

    passcode = models.CharField(
        max_length=6,
        validators=[
            validate_passcode,
        ],

    )

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )
