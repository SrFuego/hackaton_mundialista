# apps/bet/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .models import UserBet
from .serializers import UserBetModelSerializer


# Create your viewsets here.
class UserBetViewSet(ModelViewSet):
    queryset = UserBet.objects.all()
    serializer_class = UserBetModelSerializer
    http_method_names = ["get", "post"]

    def get_serializer_class(self):
        privacy = self.request.query_params.get("privacy")
        queryset = super(UserBetViewSet, self).get_queryset()
        if privacy:
            privacity_filters = {
                "privacity_status": privacy,
                "is_active": True}
            if privacy == "privado":
                privacity_filters["user"] = self.request.user
            return queryset.filter(**privacity_filters)
        return queryset.none()
