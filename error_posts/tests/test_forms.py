from django.test import TestCase

from error_posts.mommy_recipes import django_traceback
from error_posts.models import ErrorPost
from error_posts.forms import ErrorPostForm


class TestErrorPostForm(TestCase):

    def setUp(self):
        self.form = ErrorPostForm
        self.params = {
            'exception_type': 'A',
            'error_message': 'A',
            'traceback': django_traceback,
            'django_version': '1.9',
            'recaptcha': 'a',
        }

    def test_save_form_success(self):
        error_post_form = self.form(self.params)
        error_post_form.save()
        error_post_count = ErrorPost.objects.count()
        self.assertEqual(error_post_count, 1)

    def test_form_is_valid(self):
        error_post_form = self.form(self.params)
        self.assertEqual(error_post_form.is_valid(), True)

    def test_save_form_create_right_object(self):
        error_post_form = self.form(self.params)
        error_post_form.save()
        error_post = ErrorPost.objects.first()
        self.assertEqual(error_post.exception_type, self.params['exception_type'])
        self.assertEqual(error_post.error_message, self.params['error_message'])
        self.assertEqual(error_post.traceback, self.params['traceback'])
        self.assertEqual(error_post.django_version, self.params['django_version'])

    def test_initialized_fields_are_readonly(self):
        error_post_form = self.form(initial=self.params)
        self.assertEqual(error_post_form['traceback'].field.widget.attrs['readonly'], True)
        self.assertEqual(error_post_form['django_version'].field.widget.attrs['readonly'], True)
        self.assertEqual(error_post_form['exception_type'].field.widget.attrs['readonly'], True)
        self.assertEqual(error_post_form['error_message'].field.widget.attrs['readonly'], True)
