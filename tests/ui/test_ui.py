from data.user import User
from package.login_page import LoginPage

from selene import browser
from selenium import webdriver

browser.config.driver_options = webdriver.ChromeOptions()
browser.config.driver_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

def test_login_form():
    user = User(
        first_name='Ivan',
        last_name='Ivanov',
        user_name='ivanoff',
        password='Test123#'
    )

    login_page = LoginPage()
    login_page.open()

    login_page.set_user_info(user)