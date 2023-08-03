from selene import have
from selene.support.shared import browser


class AlertsPage:

    def open(self):
        browser.open('/alerts')
        browser.driver.execute_script("$('#fixedban').remove()")
        return self

    def click_btn_with_confirm_ok(self):
        browser.element('#confirmButton').click()
        return self

    def assert_confirm_alert_ok(self):
        browser.driver.switch_to.alert.accept()
        browser.element('#confirmResult').should(have.text("You selected Ok"))
        return self

    def click_btn_with_confirm_cancel(self):
        browser.element('#confirmButton').click()
        return self

    def assert_confirm_alert_cancel(self):
        browser.driver.switch_to.alert.dismiss()
        browser.element('#confirmResult').should(have.text("You selected Cancel"))
        return self

    def click_btn_with_prompt(self):
        browser.element('#promtButton').click()
        return self

    def type_to_alert(self, text):
        browser.driver.switch_to.alert.send_keys(text)
        browser.driver.switch_to.alert.accept()
        return self

    def assert_prompt_alert(self, text):
        browser.element('#promptResult').should(have.text(f"You entered {text}"))
        return self