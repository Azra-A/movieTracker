from django.core.validators import MinValueValidator
from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=False,
        null=False,
    )
    release_year = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1900)],
    )
    poster_url = models.URLField(
        blank=False,
        null=False,
    )
    genres = models.ManyToManyField(
        to=Genre,
        related_name='movies',
    )

    def __str__(self):
        return self.title
