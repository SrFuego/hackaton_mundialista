# apps/geolocation/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import Continent, Country
from .serializers import ContinentModelSerializer, CountryModelSerializer


# Create your viewsets here.
class ContinentViewSet(ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentModelSerializer
    filter_fields = ("code",)


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer
    filter_fields = ("code", "continent")
