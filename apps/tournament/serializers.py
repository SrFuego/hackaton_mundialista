# apps/tournament/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Match


# Create your serializers here.
class MatchModelSerializer(ModelSerializer):

    class Meta:
        model = Match
        fields = ("country_1", "country_2", "date", "stadium", "status",)
