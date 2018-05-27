# apps/tournament/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import Match
from .serializers import MatchModelSerializer


# Create your viewsets here.
class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchModelSerializer
    http_method_names = ["get"]
