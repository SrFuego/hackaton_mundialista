# apps/tournament/models.py
# Python imports


# Django imports
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Stadium(TimeStampedModel):
    city = models.CharField(max_length=50)
    image = models.URLField(max_length=200)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Estadio"

    def __str__(self):
        return self.name


class Match(TimeStampedModel):
    STATUS_CHOICES = (
        ("scheduled", "Programado"),
        ("in progress", "En progreso"),
        ("finished", "Terminado"),
    )

    country_1 = models.ForeignKey(
        "geolocation.Country", related_name="country_1")
    country_2 = models.ForeignKey(
        "geolocation.Country", related_name="country_2")
    date = models.DateTimeField()
    stadium = models.ForeignKey("Stadium")
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)

    class Meta:
        verbose_name = "Partido"

    def __str__(self):
        return "{0} vs {1}".format(self.country_1.name, self.country_2.name)
