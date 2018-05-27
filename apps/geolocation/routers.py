# apps/geolocation/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import ContinentViewSet, CountryViewSet


# Create your routers here.
geolocalization = (
    (r"continent", ContinentViewSet),
    (r"country", CountryViewSet),
)
