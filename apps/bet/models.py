from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from django.db import models

from apps.tournament.models import Match
from apps.geolocation.models import Country


class UserBet(TimeStampedModel):
    PRIVACITY_CHOICES = (
        ("privado", "PRIVADO"),
        ("publico", "PUBLICO"),
    )
    SCORE_CHOICES = (
        ("marcador", "marcador"),
        ("ganador", "GANADOR"),
    )
    BET_CHOICES = (
        ("dinero", "DINERO"),
        ("reto", "RETO"),
    )
    null_field = {'null': True, 'blank': True}

    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        db_index=True,
        on_delete=models.SET_NULL,
    )
    match = models.ForeignKey(
        Match,
        null=True,
        blank=True,
        db_index=True,
        on_delete=models.SET_NULL
    )
    country = models.ForeignKey(
        Country,
        null=True,
        blank=True,
        db_index=True,
        on_delete=models.SET_NULL
    )
    is_active = models.BooleanField(
        "Esta activo",
        default=True
    )
    privacity_status = models.CharField(
        choices=PRIVACITY_CHOICES,
        max_length=20
    )
    score_status = models.CharField(
        choices=SCORE_CHOICES,
        max_length=20
    )
    bet_status = models.CharField(
        choices=BET_CHOICES,
        max_length=20
    )
    rode = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=6
    )
    challenge = models.TextField(**null_field)
    score_favor = models.IntegerField(**null_field)
    score_against = models.IntegerField(**null_field)

    class Meta:
        verbose_name = 'Apuestas'
