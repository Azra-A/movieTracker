from django.db import models


class Profile(models.Model):
    class RegionChoices(models.TextChoices):
        EUROPE = 'Europe', 'Europe'
        NORTH_AMERICA = 'North America', 'North America'
        SOUTH_AMERICA = 'South America', 'South America'
        ASIA = 'Asia', 'Asia'
        AFRICA = 'Africa', 'Africa'
        OCEANIA = 'Oceania', 'Oceania'
        OTHER = 'Other', 'Other'

    username = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    bio = models.TextField(
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
    region = models.CharField(
        max_length=20,
        choices=RegionChoices.choices,
    )
    activated_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.username
