from django.core.validators import MaxLengthValidator, MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import AuthorManager


class Author(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(100)
        ]
    )

    email = models.EmailField(
        unique=True,
    )

    is_banned = models.BooleanField(
        default=False,
    )

    birth_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2005),
        ]
    )

    website = models.URLField(
        null=True,
        blank=True
    )

    objects = AuthorManager()

    def __str__(self):
        return self.full_name


class Article(models.Model):
    class CATEGORIES(models.TextChoices):
        Technology = 'Technology'
        Science = 'Science'
        Education = 'Education'

    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(200)
        ]
    )

    content = models.TextField(
        validators=[MinLengthValidator(10)],
    )

    category = models.CharField(
        max_length=10,
        choices=CATEGORIES.choices,
        validators=[MaxLengthValidator(10)],
        default='Technology'
    )

    authors = models.ManyToManyField(
        to='Author',
    )

    published_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    content = models.TextField(
        validators=[MinLengthValidator(10)],
    )

    rating = models.FloatField(
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0),
        ]
    )

    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
    )

    article = models.ForeignKey(
        to='Article',
        on_delete=models.CASCADE,
    )

    published_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    def __str__(self):
        return f'Review for author {self.author.full_name} for article {self.article.title}'


























