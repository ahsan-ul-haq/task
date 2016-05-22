""" API v1 URLs. """
from rest_framework.routers import DefaultRouter

from backend.api.v1.views import UserInfoViewset


router = DefaultRouter()
router.register(r'userinfo', UserInfoViewset)
urlpatterns = router.urls
