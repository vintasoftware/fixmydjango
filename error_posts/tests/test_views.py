import pytest
from django.test import TestCase
from django.core.urlresolvers import reverse


@pytest.mark.usefixtures('client')
class ErrorPostListViewTest(TestCase):
    fixtures = ['example_data']

    def test_returns_200_and_has_errorpost_list(self):
        response = self.client.get(reverse('error_posts:list'))
        assert response.status_code == 200
        assert 'errorpost_list' in response.context
        assert len(response.context['errorpost_list']) > 0
