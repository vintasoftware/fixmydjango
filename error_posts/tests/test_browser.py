import pytest
from django.core.urlresolvers import reverse


@pytest.mark.slow
@pytest.mark.usefixtures('example_data', 'live_server', 'webdriver')
def test_on_browser(live_server, webdriver):
    webdriver.get(live_server.url + reverse('error_posts:list'))
    all_items = webdriver.find_elements_by_css_selector('.error-post-list-row .list-group-item')
    assert len(all_items) > 0
