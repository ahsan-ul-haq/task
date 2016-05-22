from rest_framework import serializers

from backend.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = UserInfo
