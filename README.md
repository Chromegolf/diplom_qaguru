# Проект автотестов UI + API

## Покрытый функционал
DemoQA - UI
- Заполнение формы студента
- Регистрация пользователя со всемми заполненными полями
- Регистрация пользователя с указанием обязательных полей
- Проверка работы с алертами страницы
- Проверка работы с тултипами страницы
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

## Выполнена интеграция проекта с Jenkins
![jenkins](/resources/jenkins.png)
- Пример интеграции проекта с Jenkins job url: https://jenkins.autotests.cloud/job/diplom/

Запуск тестов (api + ui) производится командой 
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

## В результате выполнения jenkins job, генерируется Allure report
![allure](/resources/allurerport.png)
- Пример отчета: https://jenkins.autotests.cloud/job/diplom/59/allure/

## Выполнена интеграция проекта с Allure TestOps
![allure](/resources/allureto.png)
- Пример отчета: https://allure.autotests.cloud/project/3582/dashboards

## По результату прогона отправляется уведомление в телеграм:
![tg bot](/resources/tg.png)


