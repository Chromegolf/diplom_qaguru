from selene import browser, have
from data.user import User

class LoginPage:
    def open(self):
        browser.open('/login')

    def set_user_info(self, first_name, last_name, user_name, password):
        browser.element("#firstname").type(first_name)
        browser.element("#lastname").type(last_name)
        browser.element("#userName").type(user_name)
        browser.element("#password").type(password)
        return self