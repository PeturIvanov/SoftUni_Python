from django.core import validators
from django.db import models

from main_app.validators import name_validator, age_validator, phone_number_validator


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[name_validator]
    )

    age = models.PositiveIntegerField(
        validators=[age_validator]
    )

    email = models.EmailField(
        error_messages={'invalid': 'Enter a valid email address'}
    )

    phone_number = models.CharField(
        max_length=13,
        validators=[phone_number_validator]
    )

    website_url = models.URLField(
        error_messages={'invalid': 'Enter a valid URL'}
    )
