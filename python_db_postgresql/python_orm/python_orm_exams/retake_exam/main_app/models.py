from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator

from main_app.managers import TennisPlayerManager


class TennisPlayer(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(5)],
    )

    birth_date = models.DateField()

    country = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
    )

    ranking = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ],
    )

    is_active = models.BooleanField(
        default=True,
    )

    objects = TennisPlayerManager()

    def __str__(self):
        return self.full_name


class Tournament(models.Model):
    class SURFACES(models.TextChoices):
        not_selected = 'Not Selected',
        clay = 'Clay',
        grass = 'Grass',
        hard_court = 'Hard Court'

    name = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(2)],
        unique=True
    )

    location = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )

    prize_money = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    start_date = models.DateField()

    surface_type = models.CharField(
        max_length=12,
        choices=SURFACES.choices,
        default='Not Selected'
    )

    def __str__(self):
        return self.name


class Match(models.Model):
    score = models.CharField(
        max_length=100,
    )

    summary = models.TextField(
        validators=[MinLengthValidator(5)],
    )

    date_played = models.DateTimeField()

    tournament = models.ForeignKey(
        to='Tournament',
        on_delete=models.CASCADE,
    )

    players = models.ManyToManyField(
        to='TennisPlayer',
        related_name='matches',
    )

    winner = models.ForeignKey(
        to='TennisPlayer',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Matches'
        verbose_name_plural = 'Matches'
