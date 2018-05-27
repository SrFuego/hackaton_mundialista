# apps/tournament/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import MatchViewSet


# Create your routers here.
tournament = (
    (r"match", MatchViewSet),
)
