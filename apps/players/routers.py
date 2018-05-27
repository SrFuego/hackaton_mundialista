# apps/players/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import PlayeretViewSet

# Create your routers here.
players = (
     (r"player", PlayeretViewSet),
)
