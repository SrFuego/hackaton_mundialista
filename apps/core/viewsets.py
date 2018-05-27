# apps/core/viewsets.py
# Python imports


# Django imports
from django.contrib.auth.models import User


# Third party apps imports
from django.contrib.auth import authenticate, login as django_login, logout
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import status
from rest_framework.response import Response

# Local imports
from .models import ProfileUser
from .serializers import UserProfileSerializer, UserSerializer


# Create your viewsets here.
class UserProfileViewSet(ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ["get", "post"]

    def perform_create(self, serializer):
        validated_data = self.request.data
        password = validated_data.get('password', '')

        data_profile = {
            "direccion": validated_data.get("direccion", ""),
            "dni": validated_data.get("dni", "")
        }
        data_user = {
            "first_name": validated_data.get("first_name", ""),
            "last_name": validated_data.get("last_name", ""),
            "username": validated_data.get("user_name", ""),
            "email": validated_data.get("email", ""),
            "password": validated_data.get("password", "")
        }
        print("data_user :: ", data_user)

        user_serializer = UserSerializer(data=data_user)
        if user_serializer.is_valid():
            print("valido")
            user_serializer.save()
            user = user_serializer.instance
            user.set_password(password)
            user.save()
            data_profile['usuario'] = user
        elif user_serializer.errors:
            for field, detail in user_serializer.errors.items():
                return Response({'error': detail[0]},
                                status=status.HTTP_400_BAD_REQUEST)

        profile = ProfileUser.objects.create(**data_profile)
        """
        for id_user in friends:
            if id_user not in [_.id for _ in profile.friends.all()]:
                profile.friends.add(id_user)
        """
        profile.save()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post"]
