from django.test import TestCase
from django.core.urlresolvers import reverse

from error_posts.mommy_recipes import non_published_recipe, published_recipe, django_traceback
from error_posts.models import ErrorPost


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

    def test_get_returns_error_post(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.context['object'].pk, 4)


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


class TestErrorPostCreateView(TestCase):
    view_name = 'error_posts:create'

    def setUp(self):
        self.view_url = reverse(self.view_name)
        self.params = {
            'exception_type': 'A',
            'error_message': 'A',
            'traceback': django_traceback,
            'django_version': '1.9',
            'g-recaptcha-response': 'a',
        }

    def test_get_returns_200(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)

    def test_create_error_post(self):
        response = self.client.post(self.view_url, data=self.params)
        error_post_count = ErrorPost.objects.count()
        self.assertEqual(error_post_count, 1)
        self.assertEqual(response.status_code, 302)

    def test_create_error_post_not_published_default(self):
        response = self.client.post(self.view_url, data=self.params)
        error_post = ErrorPost.objects.first()
        self.assertEqual(error_post.is_published, False)
        self.assertEqual(response.status_code, 302)

    def test_get_error_post_create_view_returns_form_initialized(self):
        querystring = (
            '?traceback=Traceback&django_version=1.9&'
            'exception_type=TemplateSyntaxError&error_message=Error'
        )
        url = '{0}{1}'.format(self.view_url, querystring)
        response = self.client.get(url)
        error_post_form = response.context['form']
        self.assertEqual(error_post_form['traceback'].value(), 'Traceback')
        self.assertEqual(error_post_form['django_version'].value(), '1.9')
        self.assertEqual(error_post_form['exception_type'].value(), 'TemplateSyntaxError')
        self.assertEqual(error_post_form['error_message'].value(), 'Error')

    def test_create_error_post_with_data_from_lib(self):
        querystring = (
            '?traceback=Traceback&django_version=1.9&'
            'exception_type=TemplateSyntaxError&error_message=Error'
        )
        url = '{0}{1}'.format(self.view_url, querystring)
        response = self.client.post(url, data=self.params)
        error_post = ErrorPost.objects.first()
        self.assertEqual(error_post.data_came_from, "lib")
        self.assertEqual(response.status_code, 302)

    def test_create_error_post_with_data_from_site(self):
        response = self.client.post(self.view_url, data=self.params)
        error_post = ErrorPost.objects.first()
        self.assertEqual(error_post.data_came_from, "site")
        self.assertEqual(response.status_code, 302)
