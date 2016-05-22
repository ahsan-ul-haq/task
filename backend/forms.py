"""
Forms for getting user name from frontend and save it in UserInfo.
"""
from django.forms import ModelForm

from backend.models import UserInfo


class UserInfoForm(ModelForm):
    """UserInfo form to save user data."""
    class Meta(object):
        model = UserInfo
        fields = ['name']
