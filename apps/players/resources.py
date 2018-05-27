# apps/players/resources.py
# Python imports


# Django imports


# Third party apps imports
from import_export.resources import ModelResource


# Local imports
from .models import Position


# Create your resources here.
class PositionResource(ModelResource):

    class Meta:
        model = Position
