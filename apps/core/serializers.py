# apps/players/serializers.py
# Python imports


# Django imports
from django.contrib.auth.models import User


# Third party apps imports
from rest_framework.serializers import (ModelSerializer, Serializer, CharField,
                                        ValidationError)


# Local imports
from .models import ProfileUser


# Create your serializers here.
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserProfileSerializer(ModelSerializer):
    usuario = UserSerializer(read_only=True)
    friends = UserSerializer(read_only=True, many=True)

    class Meta:
        model = ProfileUser
        fields = "__all__"


class ChangePasswordSerializer(Serializer):
    password = CharField(max_length=200, required=True)
    repeat_password = CharField(max_length=200, required=True)

    def validate(self, attrs):
        password = attrs.get('password', '')
        repeat_password = attrs.get('repeat_password', '')

        if password != repeat_password:
            raise ValidationError(
                'Contraseñas ingresadas no coinciden')

        return attrs
