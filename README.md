# Проект автотестов UI + API

## Покрытый функционал
DemoQA - UI
- Заполнение формы студента
- Авторизация пользователя
- Выход пользователя

reqres - API
- Создание пользователя
- Обновление пользователя
- Получение общего количества пользователей
- Регистрация пользователя без пароля
- Успешная регистрация пользователя
- Получение списка пользователей
- Получение количества пользователей на странице
- Поиск не существующего пользователя

## Запуск тестов в Jenkins
Jenkins job url: https://jenkins.autotests.cloud/job/diplom/
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

В результате генерируется allure-отчет
- Пример отчета: https://jenkins.autotests.cloud/job/diplom/59/allure/

По результату прогона отправляется уведомление в телеграм:

!(https://github.com/Chromegolf/diplom_qaguru/blob/master/resources/tg.png)
