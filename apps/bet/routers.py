# apps/geolocation/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import UserBetViewSet


# Create your routers here.
bet = (
    (r"userbet", UserBetViewSet),
)
