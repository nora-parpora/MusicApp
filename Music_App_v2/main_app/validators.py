from django.core.exceptions import ValidationError


def validate_only_letters_nums_underscore(value):
    for l in value:
        if not l.isalpha() and not l.isnum() and not "_":
            raise ValidationError(f"Ensure this value contains only letters, numbers, and underscore.")


def validate_only_positive_numbers(value):
    if value < 0:
        raise ValidationError(f"Price cannot be negative!")


def validate_age_has_only_positive_integers(value):
    if value < 0:
        raise ValidationError(f"The age cannot be negative!")