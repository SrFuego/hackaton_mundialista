# apps/tournament/resources.py
# Python imports


# Django imports


# Third party apps imports
from import_export.resources import ModelResource


# Local imports
from .models import Stadium


# Create your resources here.
class StadiumResource(ModelResource):

    class Meta:
        model = Stadium
