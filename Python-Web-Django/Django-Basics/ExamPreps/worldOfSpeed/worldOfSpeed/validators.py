from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_chars_username(username):
    for ch in username:
        if not ch.isalnum() and ch != '_':
            raise ValidationError("Username must contain only letters, digits, and underscores!")

@deconstructible
class ValidateCharsUsername:

    def __call__(self, value):
        for ch in value:
            if not ch.isalnum() and ch != '_':
                raise ValidationError("Username must contain only letters, digits, and underscores!")