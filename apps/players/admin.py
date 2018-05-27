# apps/players/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports
from import_export.admin import ImportExportModelAdmin


# Local imports
from .models import Position
from .resources import PositionResource


# Register your models here.
@admin.register(Position)
class PositionAdmin(ImportExportModelAdmin):
    resource_class = PositionResource
