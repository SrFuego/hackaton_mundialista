from django.contrib.auth.models import User

# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import ProfileUser


# Create your serializers here.

class UserSerializer(ModelSerializer):

    def create(self, validated_data):
        password = validated_data.data.get('password', '')
        data_profile = {
            'direccion': validated_data.data.get('direccion', ''),
            'dni': validated_data.data.get('document_number', ''),
        }

        data_user = {
            'first_name': validated_data.data.get('first_name', ''),
            'last_name': validated_data.data.get('last_name', ''),
            'username': validated_data.data.get('username', ''),
            'email': validated_data.data.get('email', ''),
            'password': validated_data.data.get('password', ''),
        }
        user = ProfileUser.objects.create(**data_user)
        user.set_password(password)
        user.save()

        data_profile['usuario'] = user
        ProfileUser.objects.create(**data_profile)
        return user

    class Meta:
        model = User
        fields = "__all__"


class UserProfileSerializer(ModelSerializer):
    usuario = UserSerializer(source='usuario', read_only=True)
    friends = UserSerializer(source='friends', read_only=True, many=True)

    class Meta:
        model = ProfileUser
        fields = "__all__"
