# apps/players/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import UserBet
from .serializers import PlayebasicrModelSerializer, PlayerModelSerializer


# Create your viewsets here.
class UserBetViewSet(ModelViewSet):
    queryset = UserBet.objects.all()
    serializer_class = PlayerModelSerializer
    http_method_names = ["get"]

    def get_serializer_class(self):
        if self.request.query_params.get('type') == 'basic':
            return PlayebasicrModelSerializer

        return PlayerModelSerializer
