# apps/bet/serializers.py
# Python imports
from rest_framework.serializers import SerializerMethodField

# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

# Local imports
from .models import UserBet


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')


# Create your serializers here.
class UserBetModelSerializer(ModelSerializer):
    all_user = SerializerMethodField('func_all_user')

    def func_all_user(self, obj):
        return UserSerializer(User.objects.all(), many=True).data

    class Meta:
        model = UserBet
        fields = ('all_user',)
