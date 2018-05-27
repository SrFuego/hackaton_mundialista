# apps/tournament/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework import serializers


# Local imports
from .models import Match, Stadium

from ..geolocation.serializers import CountryModelSerializer


# Create your serializers here.
class StadiumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ("id", "name", "city", "image",)


class MatchModelSerializer(serializers.ModelSerializer):
    country_1 = CountryModelSerializer()
    country_2 = CountryModelSerializer()
    stadium = StadiumModelSerializer()

    class Meta:
        model = Match
        fields = ("id", "country_1", "country_2", "date", "stadium", "status",)
