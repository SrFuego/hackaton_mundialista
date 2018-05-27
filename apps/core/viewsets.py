# apps/core/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import ProfileUser
from .serializers import UserProfileSerializer


# Create your viewsets here.
class UserBetViewSet(ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ["get", "post"]

