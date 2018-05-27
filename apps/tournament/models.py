# apps/tournament/models.py
# Python imports


# Django imports
from django.db import models


# Third party apps imports
from model_utils.models import TimeStampedModel
from apps.players.models import Player

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


class Group(TimeStampedModel):
    name = models.CharField(max_length=5, unique=True)
    winner = models.ForeignKey(
        "geolocation.Country", related_name="winner", blank=True, null=True)
    runnerup = models.ForeignKey(
        "geolocation.Country", related_name="runnerup", blank=True, null=True)

    class Meta:
        verbose_name = "Grupo"

    def __str__(self):
        return self.name


class Incident(TimeStampedModel):
    KIND_CHOICES = (
        ("goal", "GOAL"),
        ("foul", "FOUL"),
        ("yellow_card", "YELLOW_CARD"),
        ("red_card", "RED_CARD"),

    )
    kind = models.CharField(max_length=10, unique=True)
    player = models.ForeignKey(Player, null=True, blank=True)

    def __str__(self):
        return '{0}-{1}'.format(
            self.kind, self.player.name if self.player else '-'
        )
