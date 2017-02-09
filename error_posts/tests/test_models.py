from django.test import TestCase
from django.core import exceptions

from error_posts.models import ErrorPost


class TestTracebackInvalid(TestCase):

    def test_invalid_traceback_raises_validation_error_on_clean(self):

        with self.assertRaises(exceptions.ValidationError):
            error_post = ErrorPost(traceback="invalid traceback")
            error_post.clean()
