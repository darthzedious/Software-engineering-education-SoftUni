from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CapitalFirstLetterValidator:
    def __call__(self, value):
        if not value[0].isupper():
            raise ValidationError("Name must start with a capital letter!")