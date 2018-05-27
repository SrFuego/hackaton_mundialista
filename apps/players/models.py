# apps/players/models.py
# Python imports


# Django imports
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel


# Local imports
from .utils import (
    get_val_card_yellow, get_val_fatigue, get_val_recover,
    get_val_serious_foul)


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
    age = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return "{0}, {1}".format(self.last_name, self.first_name)


class Player(Person):
    acceleration = models.PositiveSmallIntegerField(blank=True, null=True)
    aggression = models.PositiveSmallIntegerField(blank=True, null=True)
    agility = models.PositiveSmallIntegerField(blank=True, null=True)
    balance = models.PositiveSmallIntegerField(blank=True, null=True)
    ball_control = models.PositiveSmallIntegerField(blank=True, null=True)
    club_name = models.CharField(max_length=50)
    club_logo = models.URLField(max_length=200)
    order_fifa = models.PositiveSmallIntegerField(blank=True, null=True)
    overall = models.PositiveSmallIntegerField(blank=True, null=True)
    points = models.PositiveSmallIntegerField(blank=True, null=True)
    potential = models.PositiveSmallIntegerField(blank=True, null=True)
    position = models.ForeignKey("Position")
    reaction = models.PositiveSmallIntegerField(blank=True, null=True)
    recover = models.PositiveSmallIntegerField(blank=True, null=True)
    selection = models.ForeignKey("geolocation.Country")
    stamina = models.PositiveSmallIntegerField(blank=True, null=True)
    strength = models.PositiveSmallIntegerField(blank=True, null=True)
    with_red_card = models.BooleanField(default=False)

    def set_points(self, kind):
        if kind == "fatigue":
            self.points += get_val_fatigue(self.stamina)
        elif kind == "recovery":
            self.points += get_val_recover(self.recover)
        elif kind == "yellow_card":
            self.points += get_val_card_yellow(self.aggression)
        elif kind == "serious_misconduct":
            self.points += get_val_serious_foul(self.recover)
        elif kind == "red_card":
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
