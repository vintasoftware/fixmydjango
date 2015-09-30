# coding: utf-8

import pytest

from django.core.urlresolvers import reverse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.slow
@pytest.mark.usefixtures('live_server', 'webdriver')
def test_create_draft_on_browser(live_server, webdriver):
    webdriver.get(live_server.url + reverse('drafts:create'))
    fields = webdriver.find_elements_by_css_selector(
        "textarea, input[type=text], input[type=email]")
    for field in fields:
        field.send_keys('draft@test.com')
    submit = webdriver.find_element_by_css_selector("button[type=submit]")
    submit.click()

    WebDriverWait(webdriver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, 'div[role=alert]'))
    )

    assert webdriver.find_element_by_css_selector("div[role=alert]")
