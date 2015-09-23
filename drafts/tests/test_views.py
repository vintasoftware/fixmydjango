# coding: utf-8

import pytest

from django.core.urlresolvers import reverse

from drafts.models import Draft


@pytest.mark.usefixtures('client')
def test_returns_200(client):
    response = client.get(reverse('drafts:create'))
    assert response.status_code == 200


@pytest.mark.usefixtures('client', 'transactional_db')
def test_post_creates_a_draft(client):
    params = {
        'author': 'not-a-real-name',
        'email': 'not-a-real@email.com',
        'exception_type': 'test-exception',
        'error_message': 'test-error-message',
        'traceback': 'test-traceback',
        'how_to_reproduce': 'how_to_repr_test',
    }
    client.post(reverse('drafts:create'), data=params)
    assert Draft.objects.all().count() == 1
