# apps/players/models.py
# Python imports


# Django imports
from django.db import models
from django.utils import timezone


# Third party apps imports
from model_utils.models import TimeStampedModel
from .utils import (get_val_card_yellow, get_val_fatigue, get_val_recover,
                    get_val_serious_foul)

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
    name = models.CharField(max_length=75, blank=True, null=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)
    ball_control = models.PositiveSmallIntegerField(blank=True, null=True)
    reactions = models.PositiveSmallIntegerField(blank=True, null=True)
    agility = models.PositiveSmallIntegerField(blank=True, null=True)
    aggression = models.PositiveSmallIntegerField(blank=True, null=True)
    aceleration = models.PositiveSmallIntegerField(blank=True, null=True)
    balance = models.PositiveSmallIntegerField(blank=True, null=True)
    club_name = models.PositiveSmallIntegerField(blank=True, null=True)
    recover = models.PositiveSmallIntegerField(blank=True, null=True)
    stamina = models.PositiveSmallIntegerField(blank=True, null=True)
    strength = models.PositiveSmallIntegerField(blank=True, null=True)
    points = models.PositiveSmallIntegerField(blank=True, null=True)
    overall = models.PositiveSmallIntegerField(blank=True, null=True)
    with_red_card = models.BooleanField(default=False)
    born_country = models.ForeignKey(
        "geolocation.Country", related_name="citizens")
    selection = models.ForeignKey(
        "geolocation.Country", related_name="players")
    position = models.ForeignKey("Position")

    def set_points(self, tipo):
        if tipo == "fatiga":
            self.points += get_val_fatigue(self.stamina)
        elif tipo == "recuperacion":
            self.points += get_val_recover(self.recover)
        elif tipo == "tarjeta_amarilla":
            self.points += get_val_card_yellow(self.aggression)
        elif tipo == "falta_grave":
            self.points += get_val_serious_foul(self.recover)
        elif tipo == "tarjeta_roja":
            self.points += -80

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
