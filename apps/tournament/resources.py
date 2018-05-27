# apps/tournament/resources.py
# Python imports


# Django imports
from django.utils.dateparse import parse_datetime


# Third party apps imports
from import_export.resources import ModelResource


# Local imports
from .models import Group, Match, Stadium
from ..geolocation.models import Country


# Create your resources here.
class MatchResource(ModelResource):
    class Meta:
        model = Match

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        i = 0
        last = dataset.height
        aux = None

        country_1_index = dataset.headers.index("country_1")
        country_2_index = dataset.headers.index("country_2")
        date_index = dataset.headers.index("date")
        stadium_index = dataset.headers.index("stadium")
        group_index = dataset.headers.index("group")

        while i < last:
            aux = list(dataset.lpop())
            try:
                aux[country_1_index] = Country.objects.get(
                    code=aux[country_1_index]).id
            except Country.DoesNotExist:
                print("no existe pais para: ", aux[country_1_index])

            try:
                aux[country_2_index] = Country.objects.get(
                    code=aux[country_2_index]).id
            except Country.DoesNotExist:
                print("no existe pais para: ", aux[country_2_index])

            aux[date_index] = parse_datetime(aux[date_index])

            try:
                aux[stadium_index] = Stadium.objects.get(
                    name=aux[stadium_index]).id
            except Stadium.DoesNotExist:
                print("no existe estadio para: ", aux[stadium_index])

            try:
                aux[group_index] = Group.objects.get(name=aux[group_index]).id
            except Group.DoesNotExist:
                print("no existe grupo para: ", aux[group_index])

            dataset.rpush(tuple(aux))
            i += 1


class StadiumResource(ModelResource):
    class Meta:
        model = Stadium
