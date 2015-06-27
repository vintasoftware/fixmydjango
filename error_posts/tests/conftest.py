import pytest
from django.core import management

from ..models import Answer, ErrorPost


@pytest.yield_fixture(scope='function')
def example_data(db):
    management.call_command(
        'loaddata',
        'error_posts/fixtures/example_data.json',
        verbosity=0)
    yield
    Answer.objects.all().delete()
    ErrorPost.objects.all().delete()


from selenium.webdriver import Firefox


@pytest.yield_fixture(scope='session')
def webdriver():
    driver = Firefox()
    yield driver
    driver.quit()
