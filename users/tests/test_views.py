from django.core.urlresolvers import reverse
from django.utils.six.moves import http_client

from core.tests.utils import FixMyDjangoTestCase
from users.models import User


class SignUpViewTest(FixMyDjangoTestCase):
    view_name = 'signup'

    def setUp(self):
        super().setUp()
        self.params = {
            'email': 'test@email.com',
            'first_name': 'first-name-test',
            'last_name': 'last-name-test',
            'password': '123'
        }

    def test_get_with_anonymous_returns_200(self):
        response = self.client.get(reverse(self.view_name))

        self.assertEqual(response.status_code, http_client.OK)

    def test_authenticated_get_redirects_to_error_list(self):
        response = self.auth_client.get(reverse(self.view_name))

        self.assertEqual(response.url, reverse('error_posts:list'))

    def test_post(self):
        response = self.client.post(reverse(self.view_name), self.params, follow=True)

        self.assertEqual(response.status_code, http_client.OK)

    def test_post_creates_an_user(self):
        self.client.post(reverse(self.view_name), self.params, follow=True)

        self.assertTrue(User.objects.get(email=self.params['email']))

    def test_post_redirects_to_error_list(self):
        response = self.client.post(reverse(self.view_name), self.params, follow=True)

        self.assertEqual(response.redirect_chain[0][0], reverse('error_posts:list'))
