import allure
from package.alerts_page import AlertsPage

alerts = AlertsPage()

@allure.title('Подтверждение алерта')
def test_confirm_alert_ok(setup_browser):
    with allure.step('Открываем страницу алертов'):
        alerts.open()
    with allure.step('Нажимаем кнопку для инциализации алерта'):
        alerts.click_btn_with_confirm_ok()
    with allure.step('Проверяем алерт'):
        alerts.assert_confirm_alert_ok()


@allure.title('Отклонение алерта')
def test_confirm_alert_cancel(setup_browser):
    with allure.step('Открываем страницу алертов'):
        alerts.open()
    with allure.step('Нажимаем кнопку для инциализации алерта'):
        alerts.click_btn_with_confirm_cancel()
    with allure.step('Проверяем алерт'):
        alerts.assert_confirm_alert_cancel()


@allure.title('Алерт с возможностью ввода текста')
def test_prompt_alert(setup_browser):
    with allure.step('Открываем страницу алертов'):
        alerts.open()
    with allure.step('Нажимаем кнопку для инциализации алерта'):
        alerts.click_btn_with_prompt()
    with allure.step('Вводим значение в поле ввода'):
        alerts.type_to_alert('antipovra')
    with allure.step('Проверяем алерт'):
        alerts.assert_prompt_alert('antipovra')