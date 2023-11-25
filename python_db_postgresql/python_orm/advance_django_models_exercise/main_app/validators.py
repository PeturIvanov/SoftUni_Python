from django.core.exceptions import ValidationError


def name_validator(value):
    split_value = value.split()

    if not all(el.isalpha() for el in split_value):
        raise ValidationError('Name can only contain letters and spaces')


def age_validator(value):
    if value < 18:
        raise ValidationError("Age must be greater than 18")


def phone_number_validator(value):
    last_nine_digits = value[4::]

    if not value.startswith('+359') or not last_nine_digits.isdigit() or len(last_nine_digits) != 9:
        raise ValidationError("Phone number must start with '+359' followed by 9 digits")

