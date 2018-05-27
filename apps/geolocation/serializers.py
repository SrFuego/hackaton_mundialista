# apps/geolocation/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Continent, Country


# Create your serializers here.
class ContinentModelSerializer(ModelSerializer):

    class Meta:
        model = Continent
        fields = ("id", "code", "name",)


class CountryModelSerializer(ModelSerializer):
    continent = ContinentModelSerializer()

    class Meta:
        model = Country
        fields = ("id", "code", "name", "continent",)
