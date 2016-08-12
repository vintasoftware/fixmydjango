from django.core.urlresolvers import reverse

from test_plus.test import TestCase


class TestDraftCreateView(TestCase):
    view_name = 'drafts:create'

    def setUp(self):
        self.view_url = reverse(self.view_name)

        self.params = {
            'author': 'The Name',
            'email': 'some@email.com',
            'exception_type': 'SomeException',
            'error_message': 'The message',
            'traceback': 'thetraceback',
            'django_version': '1.9',
            'g-recaptcha-response': 'a'
        }

    def test_get_returns_200(self):
        self.assertGoodView(self.view_name)

    def test_creates_draft(self):
        self.post(self.view_name, data=self.params)
        self.response_302()
