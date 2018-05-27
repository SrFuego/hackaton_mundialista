# apps/geolocation/resources.py
# Python imports


# Django imports


# Third party apps imports
from import_export.resources import ModelResource


# Local imports
from .models import Continent, Country


# Create your resources here.
class ContinentResource(ModelResource):

    class Meta:
        model = Continent


class CountryResource(ModelResource):

    class Meta:
        model = Country

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        i = 0
        last = dataset.height
        aux = None
        continent_index = dataset.headers.index("continent")

        while i < last:
            aux = list(dataset.lpop())
            try:
                aux[continent_index] = Continent.objects.get(
                    code=aux[continent_index]).id
            except Continent.DoesNotExist:
                print("no existe continente para: ", aux[continent_index])

            dataset.rpush(tuple(aux))
            i += 1
