# apps/core/models.py
# Python imports


# Django imports
from django.contrib.auth.models import User
from django.db import models


# Third party apps imports


# Local imports


# Create your models here.
class ProfileUser(models.Model):
    usuario = models.OneToOneField(User, models.CASCADE, related_name="perfil")
    dni = models.CharField(max_length=8, blank=False, null=False)
    friends = models.ManyToManyField(User, null=True, blank=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.usuario.username
