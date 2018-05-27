# apps/bet/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import UserBet


# Create your serializers here.
class UserBetModelSerializer(ModelSerializer):

    class Meta:
        model = UserBet
        fields = "__all__"
