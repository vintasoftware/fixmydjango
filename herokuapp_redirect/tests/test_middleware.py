from collections import OrderedDict

from django.test import TestCase, RequestFactory, override_settings
from django.http import HttpResponseRedirect

from herokuapp_redirect.middleware import CustomDomainRedirectMiddleware


class TestAuthenticationMiddleware(TestCase):

    def setUp(self):
        self.middleware = CustomDomainRedirectMiddleware(get_response=lambda r: r)
        self.factory = RequestFactory()

    def test_does_nothing_if_herokuapp_not_in_host(self):
        request = self.factory.get('/example/')
        request.META['HTTP_HOST'] = 'example.org'
        processed_request = self.middleware(request)
        self.assertEqual(processed_request, request)

    @override_settings(PROTOCOL='http', DOMAIN='example.org')
    def test_does_redirect_to_host_if_herokuapp_in_host(self):
        query_data = OrderedDict([
            ('a', [1, 2]),
            ('b', 'test'),
        ])
        request = self.factory.get('/example/', data=query_data)
        request.META['HTTP_HOST'] = 'example.herokuapp.com'
        response = self.middleware(request)
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response['location'], 'http://example.org/example/?a=1&a=2&b=test')
