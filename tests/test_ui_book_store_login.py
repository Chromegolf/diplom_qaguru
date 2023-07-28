from data.users_book_store import BookUser
from package.login_page import LoginPage
from utils import attach
import allure
from selene import browser
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options

@allure.tag('ui')
@allure.title('Авторизация пользователя')
def test_login_form():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="http://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    user = BookUser(
        username='Ivanoff',
        password='Test123#',
    )

    login_page = LoginPage()

    with allure.step("Открываем страницу авторизации"):
        login_page.open()

    # WHEN
    with allure.step("Выполняем авторизацию пользователя"):
        login_page.auth(user)

    with allure.step("Выполняем выход пользователя"):
        login_page.exit()

    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
