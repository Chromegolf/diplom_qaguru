from selene import browser
from data.users_book_store import BookUser

class LoginPage:

    def open(self):
        browser.open('/login')

    def set_user_info(self, username, password):
        browser.element("#userName").type(username)
        browser.element("#password").type(password)
        return self

    def auth(self, user: BookUser):
        self.set_user_info(user.username, user.password)
        browser.element("#login").click()

    def go_to_auth(self):
        browser.element("#login").click()

    def exit(self):
        browser.element("#submit").click()
