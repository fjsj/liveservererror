import requests
from django.core.urlresolvers import reverse
from django.test.utils import override_settings
from django.test import LiveServerTestCase


class LoginTestCase(LiveServerTestCase):

    @override_settings(DEBUG=True)
    def test_login(self):
        response = requests.get(self.live_server_url + reverse('test-error'))

        self.assertEqual(response.status_code, 500)
