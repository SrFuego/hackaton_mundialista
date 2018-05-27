# apps/players/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports
from import_export.admin import ImportExportModelAdmin


# Local imports
from .models import Player, Position
from .resources import PlayerResource, PositionResource


# Register your models here.
@admin.register(Player)
class PlayerAdmin(ImportExportModelAdmin):
    resource_class = PlayerResource


@admin.register(Position)
class PositionAdmin(ImportExportModelAdmin):
    resource_class = PositionResource
