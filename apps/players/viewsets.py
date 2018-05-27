# apps/players/viewsets.py
# Python imports


# Django imports
from django.db.models import Q

# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import Player
from .serializers import PlayerBasicModelSerializer, PlayerModelSerializer


# Create your viewsets here.
class PlayeretViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerModelSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        name = self.request.query_params('name')
        queryset = super(PlayeretViewSet, self).get_queryset()
        if name:
            return queryset.filter(
               Q(first_name__icontains=name) | Q(last_name__icontains=name)
            )

        return queryset

    def get_serializer_class(self):
        if self.request.query_params.get("type") == "basic":
            return PlayerBasicModelSerializer
        return PlayerModelSerializer
