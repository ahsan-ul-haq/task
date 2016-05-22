"""
Urls for backend app.
"""
from django.conf.urls import patterns, url

from backend.views import UserInfoView


urlpatterns = patterns('',
                       url(r'^$', UserInfoView.as_view(), name='user_info'),
                       )
