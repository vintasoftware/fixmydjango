from django.test import TestCase
from django.core.urlresolvers import reverse



class TestErrorPostListView(TestCase):
    view_name = 'error_posts:list'

    def setUp(self):
        self.view_url = reverse(self.view_name)

    def test_get_returns_200(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)



class TestErrorPostDetailView(TestCase):
    fixtures = ['example_data.json']
    view_name = 'error_posts:detail'

    def setUp(self):
        self.view_url = reverse(self.view_name, kwargs={'slug': 'core-mail-message-valueerror'})

    def test_get_returns_200(self):
        response = self.client.get(self.view_url)

        self.assertEqual(response.status_code, 200)
