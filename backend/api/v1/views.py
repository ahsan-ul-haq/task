from rest_framework import viewsets

from backend.api.serializers import UserInfoSerializer
from backend.models import UserInfo


class UserInfoViewset(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
