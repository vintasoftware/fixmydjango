from django.test import TestCase

from error_posts.mommy_recipes import django_traceback
from error_posts.models import ErrorPost
from error_posts.forms import ErrorPostForm

from django_comments.models import Comment
from django_comments.forms import CommentSecurityForm
from error_posts.forms import CommentFormWithMarkDown
from model_mommy import mommy
from users.models import User


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


class TestCommentForm(TestCase):

    def setUp(self):
        self.form = CommentFormWithMarkDown
        self.params = {
            'name': 'Alessandro',
            'email': 'alessandro.henrique@labcodes.com.br',
            'comment': 'This is a simple comment',
        }
        self.user = mommy.make(User)
        self.security_dict = CommentSecurityForm(self.user).generate_security_data()
        self.params.update(self.security_dict)
        self.comment = mommy.make(Comment)


    def test_form_is_valid(self):
        comment_form = self.form(data=self.params, target_object=self.comment)
        self.assertEqual(comment_form.is_valid(), True)
