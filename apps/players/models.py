# apps/players/models.py
# Python imports


# Django imports
from django.db import models
from django.utils import timezone


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports


# Create your models here.
class Position(TimeStampedModel):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)

    class Meta:
        verbose_name = "Posición"
        verbose_name_plural = "Posiciones"

    def __str__(self):
        return self.name


class Person(TimeStampedModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    born_date = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return "{0}, {1}".format(self.last_name, self.first_name)

    @property
    def age(self):
        today = timezone.now()
        born = self.born_date
        already_birthday = ((today.month, today.day) < (born.month, born.day))
        return today.year - born.year - already_birthday


class Player(Person):
    ball_control = models.PositiveSmallIntegerField(blank=True, null=True)
    born_country = models.ForeignKey(
        "geolocation.Country", related_name="citizens")
    selection = models.ForeignKey(
        "geolocation.Country", related_name="players")
    position = models.ForeignKey("Position")

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"


class TechnicalDirector(Person):
    born_country = models.ForeignKey(
        "geolocation.Country", related_name="technical_director")
    selection = models.OneToOneField("geolocation.Country")

    class Meta:
        verbose_name = "Director Técnico"
        verbose_name_plural = "Directores Técnicos"
