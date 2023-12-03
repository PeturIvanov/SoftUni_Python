from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator, MinLengthValidator

from main_app.managers import DirectorManager


class Person(models.Model):

    class Meta:
        abstract = True

    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    birth_date = models.DateField(
        default='1900-01-01'
    )

    nationality = models.CharField(
        max_length=50,
        default='Unknown'
    )


class Director(Person):

    years_of_experience = models.SmallIntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )

    objects = DirectorManager()

    def __str__(self):
        return self.full_name


class Actor(Person):
    is_awarded = models.BooleanField(
        default=False
    )

    last_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.full_name


class Movie(models.Model):
    class GENRES(models.TextChoices):
        action = 'Action',
        comedy = 'Comedy',
        drama = 'Drama',
        other = 'Other'

    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)]
    )

    release_date = models.DateField()

    storyline = models.TextField(
        blank=True,
        null=True
    )

    genre = models.CharField(
        max_length=6,
        choices=GENRES.choices,
        default='Other'
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        default=0
    )

    is_classic = models.BooleanField(
        default=False
    )

    is_awarded = models.BooleanField(
        default=False
    )

    last_updated = models.DateTimeField(
        auto_now=True
    )

    director = models.ForeignKey(
        to='Director',
        on_delete=models.CASCADE
    )

    starring_actor = models.ForeignKey(
        to='Actor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    actors = models.ManyToManyField(
        to='Actor',
        related_name='movies'
    )

    def __str__(self):
        return self.title


































