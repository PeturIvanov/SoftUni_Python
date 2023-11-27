from django.contrib.postgres.search import SearchVectorField
from django.core import validators
from django.db import models
from decimal import Decimal

from main_app.mixins import RechargeEnergyMixin
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


class BaseMedia(models.Model):

    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']

    title = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    genre = models.CharField(
        max_length=50,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Book(BaseMedia):

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Book'
        verbose_name_plural = 'Models of type - Book'

    author = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(5, message='Author must be at least 5 characters long')
        ]
    )

    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            validators.MinLengthValidator(6, message='ISBN must be at least 6 characters long')
        ]
    )


class Movie(BaseMedia):

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Movie'
        verbose_name_plural = 'Models of type - Movie'

    director = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(8, message='Director must be at least 8 characters long')
        ]
    )


class Music(BaseMedia):

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Music'
        verbose_name_plural = 'Models of type - Music'

    artist = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(9, message='Artist must be at least 9 characters long')
        ]
    )


class Product(models.Model):
    name = models.CharField(
        max_length=100,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def calculate_tax(self) -> Decimal:
        return self.price * Decimal(0.08)

    @staticmethod
    def calculate_shipping_cost(weight: Decimal) -> Decimal:
        return weight * Decimal(2.00)

    def format_product_name(self) -> str:
        return f'Product: {self.name}'


class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def calculate_price_without_discount(self) -> Decimal:
        original_price = self.price * Decimal(1.20)

        return original_price

    def calculate_tax(self) -> Decimal:
        tax = self.price * Decimal(0.05)

        return tax

    @staticmethod
    def calculate_shipping_cost(weight: Decimal) -> Decimal:
        shipping_cost = weight * Decimal(1.50)

        return shipping_cost

    def format_product_name(self) -> str:
        result = f'Discounted Product: {self.name}'

        return result


class Hero(models.Model, RechargeEnergyMixin):

    name = models.CharField(
        max_length=100,
    )

    hero_title = models.CharField(
        max_length=100,
    )

    energy = models.PositiveIntegerField()


class SpiderHero(Hero):

    class Meta:
        proxy = True

    def swing_from_buildings(self) -> str:
        if self.energy - 80 <= 0:
            return f'{self.name} as Spider Hero is out of web shooter fluid'

        self.energy -= 80
        self.save()
        return f'{self.name} as Spider Hero swings from buildings using web shooters'


class FlashHero(Hero):

    class Meta:
        proxy = True

    def run_at_super_speed(self) -> str:
        if self.energy - 65 <= 0:
            return f'{self.name} as Flash Hero needs to recharge the speed force'

        self.energy -= 65
        self.save()

        return f'{self.name} as Flash Hero runs at lightning speed, saving the day'


class Document(models.Model):
    title = models.CharField(
        max_length=200,
    )

    content = models.TextField()

    search_vector = SearchVectorField(
        null=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=['search_vector'])
        ]

