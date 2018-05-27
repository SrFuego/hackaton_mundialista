# apps/tournament/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response


# Local imports
from .models import Incident, Match, Player
from .serializers import IncidentModelSerializer, MatchModelSerializer


# Create your viewsets here.
class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchModelSerializer
    http_method_names = ["get"]


class IncidentViewSet(ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        player = Player.objects.get(id=request.data["player"])
        player.set_points(request.data["kind"])
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers)
