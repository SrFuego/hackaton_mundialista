# apps/geolocation/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports
from import_export.admin import ImportExportModelAdmin


# Local imports
from .models import Continent, Country
from .resources import ContinentResource, CountryResource


# Register your models here.
@admin.register(Continent)
class ContinentAdmin(ImportExportModelAdmin):
    resource_class = ContinentResource


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource
