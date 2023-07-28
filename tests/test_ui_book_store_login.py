from data.users_book_store import BookUser
from package.login_page import LoginPage
from utils import attach
import allure
from selene import browser


@allure.tag('ui')
@allure.title('Авторизация пользователя')
def test_login_form():
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
