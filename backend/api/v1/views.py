from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from backend.api.serializers import UserInfoSerializer
from backend.models import UserInfo


class UserInfoViewset(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    authentication_classes = (TokenAuthentication,)
