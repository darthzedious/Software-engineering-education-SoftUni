from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models

from worldOfSpeed.car_app.choices import CarChoices
from worldOfSpeed.profile_app.models import Profile


class Car(models.Model):
    TYPE_MAX_LEN = 10
    MODEL_MAX_CHAR = 15
    MODEL_MIN_CHAR = 1

    MIN_YEAR = 1999
    MAX_YEAR = 2030

    MIN_PRICE = 1.0

    ERROR_MESSAGE_YEAR = f"Year must be between {MIN_YEAR} and {MAX_YEAR}!"


    type = models.CharField(
        null=False,
        blank=False,
        max_length=TYPE_MAX_LEN,
        choices=CarChoices,
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=MODEL_MAX_CHAR,
        validators=[MinLengthValidator(MODEL_MIN_CHAR),
        ],
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[MaxValueValidator(MAX_YEAR, message=ERROR_MESSAGE_YEAR),
                    MinValueValidator(MIN_YEAR, message=ERROR_MESSAGE_YEAR),
        ]
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        unique=True,
        verbose_name='Image URL'
    )

# o	Image URL
# 	URL field, required, unique.
# 	A placeholder: "https://..."
# 	A custom error message for unique constraint: "This image URL is already in use! Provide a new one."

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_PRICE)
        ],
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )
