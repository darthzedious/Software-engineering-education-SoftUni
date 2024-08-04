from django.core.exceptions import ValidationError


def valid_name(value):
    for letter in value:
        if not (letter.isalpha() or letter.isspace()):
            raise ValidationError("Name can only contain letters and spaces")
