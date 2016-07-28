from django.test import TestCase
from django.core.urlresolvers import reverse



class TestDraftCreateView(TestCase):
    view_name = 'drafts:create'

    def setUp(self):
        self.view_url = reverse(self.view_name)

    def test_get_returns_200(self):
        response = self.client.get(self.view_url)

        self.assertEqual(response.status_code, 200)
