from selene import have
from selene.support.shared import browser


class TooltipPage:

    def open(self):
        browser.open('/tool-tips')
        browser.driver.execute_script('$("#fixedban").remove()')
        return self

    def set_focus_in_field(self):
        browser.element('#toolTipTextField').click()
        return self

    def assert_text_field(self):
        browser.element('div.tooltip').should(have.text('You hovered over the text field'))
        return self