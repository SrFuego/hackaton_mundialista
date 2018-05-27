# apps/players/resources.py
# Python imports


# Django imports


# Third party apps imports
from import_export.resources import ModelResource


# Local imports
from .models import Player, Position
from ..geolocation.models import Country


# Create your resources here.
class PlayerResource(ModelResource):

    class Meta:
        model = Player

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        i = 0
        last = dataset.height
        aux = None

        countries_names = list(set(
            Country.objects.all().values_list("name", flat=True)))

        position_index = dataset.headers.index("position")
        selection_index = dataset.headers.index("selection")

        while i < last:
            aux = list(dataset.lpop())

            if aux[selection_index] in countries_names:
                try:
                    aux[position_index] = Position.objects.get(
                        code=aux[position_index]).id
                except Position.DoesNotExist:
                    print("no existe posicion para: ", aux[position_index])

                try:
                    aux[selection_index] = Country.objects.get(
                        name=aux[selection_index]).id
                except Country.DoesNotExist:
                    print("no existe seleccion para: ", aux[selection_index])

                dataset.rpush(tuple(aux))
            i += 1


class PositionResource(ModelResource):

    class Meta:
        model = Position
