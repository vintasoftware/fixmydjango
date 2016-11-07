from django.test import TestCase
from django.core.urlresolvers import reverse

from error_posts.mommy_recipes import non_published_recipe, published_recipe


class TestErrorPostListView(TestCase):
    view_name = 'error_posts:list'

    def setUp(self):
        self.view_url = reverse(self.view_name)

    def test_get_returns_200(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)

    def test_get_returns_only_publisheds_error_posts(self):
        published = published_recipe.make()
        non_published_recipe.make()
        response = self.client.get(self.view_url)
        error_posts = response.context['object_list']
        self.assertEqual(len(error_posts), 1)
        self.assertEqual(error_posts[0].pk, published.pk)


class TestErrorPostDetailView(TestCase):
    fixtures = ['example_data.json']
    view_name = 'error_posts:detail'

    def setUp(self):
        self.view_url = reverse(
            self.view_name, kwargs={'slug': 'core-mail-message-valueerror'}
        )

    def test_get_returns_200(self):
        response = self.client.get(self.view_url)

        self.assertEqual(response.status_code, 200)


class TestErrorPostNonPublishedListView(TestCase):
    view_name = 'error_posts:non_published_list'

    def setUp(self):
        self.view_url = reverse(self.view_name)

    def test_get_returns_200(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)

    def test_get_returns_only_non_publisheds_error_posts(self):
        published_recipe.make()
        non_published = non_published_recipe.make()
        response = self.client.get(self.view_url)
        error_posts = response.context['object_list']
        self.assertEqual(len(error_posts), 1)
        self.assertEqual(error_posts[0].pk, non_published.pk)
