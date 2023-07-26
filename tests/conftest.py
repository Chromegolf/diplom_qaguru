import pytest
from selene import browser

BASE_URL = 'https://reqres.in/api/'
USER_EMAIL = 'eve.holt@reqres.in'
USER_PASSWORD = 'pistol'
@pytest.fixture(scope="module", autouse=True)
def set_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'