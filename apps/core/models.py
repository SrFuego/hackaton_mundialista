# apps/core/models.py
# Python imports


# Django imports
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from django.db import models


# Third party apps imports


# Local imports


# Create your models here.
class ProfileUser(models.Model):
    usuario = models.OneToOneField(User, models.CASCADE, related_name="perfil")
    dni = models.CharField(max_length=8, blank=False, null=False)
    friends = models.ManyToManyField(User, blank=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.usuario.username if self.usuario else '-'


class Confirmed(TimeStampedModel):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        db_index=True,
        on_delete=models.SET_NULL,
    )
    is_active = models.BooleanField(
        "Esta activo",
        default=True
    )
    hash_time = models.CharField(
        "Código",
        max_length=254,
        null=True,
        blank=True
    )
    email = models.CharField(
        "Email",
        max_length=254,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Recuperacion de Contraseña'
