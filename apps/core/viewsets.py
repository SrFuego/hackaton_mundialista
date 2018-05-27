# apps/core/viewsets.py
# Python imports


# Django imports
from django.contrib.auth.models import User

# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import ProfileUser
from .serializers import UserProfileSerializer, UserSerializer


# Create your viewsets here.
class UserProfileViewSet(ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ["get", "post"]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post"]

