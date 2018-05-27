# apps/geolocation/models.py
# Python imports


# Django imports
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Iso(TimeStampedModel):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Continent(Iso):
    pass

    class Meta:
        verbose_name = "Continente"


class Country(Iso):
    continent = models.ForeignKey("Continent")
    image = models.URLField(max_length=200)

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
