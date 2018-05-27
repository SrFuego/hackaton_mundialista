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
    lookup_field = "code"
    http_method_names = ["get"]


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer
    lookup_field = "code"
    filter_fields = ("continent",)
    http_method_names = ["get"]
