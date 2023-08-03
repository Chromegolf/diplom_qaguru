from selene import browser, have

class BookPage:

    def search_book(self):
        browser.open('/books')
        browser.element("#searchBox").type('Understanding ECMAScript 6')
        browser.element(".action-buttons").click()

    def get_book(self):
        browser.all("div[class='text-right fullButton']").element_by(have.exact_text('Add To Your Collection')).click()
        return self

    def accept_alert(self):
        browser.driver.switch_to.alert.accept()
        return self

    def delete_book(self):
        browser.open('/profile')
        browser.element('#delete-record-undefined').click()
        browser.element('#closeSmallModal-ok').click()
        browser.driver.switch_to.alert.accept()
        return self
