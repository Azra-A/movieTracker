from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    rating = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    movie = models.ForeignKey(
        to='movies.Movie',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    profile = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    def __str__(self):
        return f"Review for {self.movie} by {self.profile}"
