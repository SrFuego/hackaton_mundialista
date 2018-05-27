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

    def create(self, validated_data):
        print("///////////////")
        print(validated_data)
        print("///////////////")
        password = validated_data.data.get('password', '')
        friends = validated_data.data.get('UserBetViewSet', [])
        data_profile = {
            "direccion": validated_data.data.get("direccion", ""),
            "dni": validated_data.data.get("document_number", "")
        }
        data_user = {
            "first_name": validated_data.data.get("first_name", ""),
            "last_name": validated_data.data.get("last_name", ""),
            "username": validated_data.data.get("username", ""),
            "email": validated_data.data.get("email", ""),
            "password": validated_data.data.get("password", "")}
        user = ProfileUser.objects.create(**data_user)
        user.set_password(password)
        user.save()

        data_profile['usuario'] = user
        profile = ProfileUser.objects.create(**data_profile)
        """
        for id_user in friends:
            if id_user not in [_.id for _ in profile.friends.all()]:
                profile.friends.add(id_user)
        """
        profile.save()
        return user


class UserProfileSerializer(ModelSerializer):
    usuario = UserSerializer(source="usuario", read_only=True)
    friends = UserSerializer(source="friends", read_only=True, many=True)

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
