import json

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from backend.models import UserInfo


class UserInfoViewSetTests(APITestCase):
    """ Test UserInfo Viewset. """

    def setUp(self):
        super(UserInfoViewSetTests, self).setUp()
        self.list_path = "http://127.0.0.1:8000/api/v1/userinfo/"
        self.user = User.objects.create(username="test")
        self.user.set_unusable_password()
        self.user.save()
        self.token = Token.objects.create(user=self.user)
        UserInfo.objects.create(name='test')
        UserInfo.objects.create(name='test 2')

    def test_get_user(self):
        """
        Verify data could be retrieve when authentication token is provided.
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = client.get(self.list_path)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['count'], 2)

    def test_get_user_unauthenticated(self):
        """
        Data could not be retrieve when authentication fails.
        """
        client = APIClient()
        response = client.get(self.list_path)
        self.assertEqual(response.status_code, 401)
