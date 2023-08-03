from data.users_book_store import BookUser
from package.login_page import LoginPage
from package.book_store_page import BookPage
import allure


@allure.tag('ui')
@allure.title('Авторизация пользователя')
def test_login_form(setup_browser):
    user = BookUser(
        username='Ivanoff',
        password='Test123#',
    )

    login_page = LoginPage()

    with allure.step("Открываем страницу авторизации"):
        login_page.open()

    with allure.step("Выполняем авторизацию пользователя"):
        login_page.auth(user)

    with allure.step("Выполняем выход пользователя"):
        login_page.exit()

