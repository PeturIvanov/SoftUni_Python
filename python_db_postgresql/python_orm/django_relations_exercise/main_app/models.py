from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=40,
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        max_length=40,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    songs = models.ManyToManyField(
        to='Song',
        related_name='artists'
    )


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    description = models.TextField(
        max_length=200,
    )

    rating = models.PositiveIntegerField()

    product = models.ForeignKey(
        to='Product',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='reviews'
    )


class Driver(models.Model):
    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class DrivingLicense(models.Model):
    license_number = models.CharField(
        max_length=10,
        unique=True,
    )

    issue_date = models.DateField()

    driver = models.OneToOneField(
        to="Driver",
        on_delete=models.CASCADE,
    )


class Owner(models.Model):
    name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(
        max_length=50,
    )

    year = models.PositiveIntegerField()

    owner = models.ForeignKey(
        to='Owner',
        on_delete=models.CASCADE,
        related_name='cars',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.model


class Registration(models.Model):
    registration_number = models.CharField(
        max_length=10,
        unique=True,
    )

    registration_date = models.DateField(
        blank=True,
        null=True,
    )

    car = models.OneToOneField(
        to='Car',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.registration_number




















