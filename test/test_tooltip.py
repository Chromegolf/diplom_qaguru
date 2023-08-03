import allure
from package.tooltip_page import TooltipPage

tooltips = TooltipPage()

@allure.title('Проверка тултипов страницы')
def test_confirm_alert_field():
    with allure.step('Открываем страницу тултипов'):
        tooltips.open()
    with allure.step('Устанавливаем фокус на поле'):
        tooltips.set_focus_in_field()
    with allure.step('Проверяем текст хинта'):
        tooltips.assert_text_field()