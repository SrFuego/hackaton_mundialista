# apps/players/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Player, Position


# Create your serializers here.
class PlayerModelSerializer(ModelSerializer):

    class Meta:
        model = Player
        fields = "__all__"


class PositionModelSerializer(ModelSerializer):

    class Meta:
        model = Position
        fields = "__all__"


class PlayerBasicModelSerializer(ModelSerializer):
    position = PositionModelSerializer(source="position", read_only=True)

    class Meta:
        model = Player
        fields = ("points", "name", "position")
