from data.user import User
from package.login_page import LoginPage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version='114.0.5708.0').install()))

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