# apps/tournament/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports
from import_export.admin import ImportExportModelAdmin


# Local imports
from .models import Match, Stadium
from .resources import StadiumResource


# Register your models here.
@admin.register(Stadium)
class StadiumAdmin(ImportExportModelAdmin):
    resource_class = StadiumResource


admin.site.register(Match)
