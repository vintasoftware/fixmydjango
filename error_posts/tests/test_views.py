import pytest
from django.core.urlresolvers import reverse


@pytest.mark.usefixtures('example_data', 'client')
def test_returns_200_and_has_errorpost_list(client):
    response = client.get(reverse('error_posts:list'))
    assert response.status_code == 200
    assert 'errorpost_list' in response.context
    assert len(response.context['errorpost_list']) > 0
