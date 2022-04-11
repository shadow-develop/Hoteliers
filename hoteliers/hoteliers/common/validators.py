from django.core.exceptions import ValidationError


def validate_letters_only(value):
    if not all(ch.isalpha() for ch in value):
        raise ValidationError('Name must contain letters only!')