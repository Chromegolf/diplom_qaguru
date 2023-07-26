import allure
from jsonschema.validators import validate
from helper import load_json_schema, CustomSession, reqres_session
##test
@allure.tag('api')
@allure.title('Получение списка пользователей')
def test_requested_page_number():
    page = 2
    schema = load_json_schema('get_requested_page_number.json')

    response = reqres_session.get('/api/users', params={'page': page})

    assert response.status_code == 200
    assert response.json()['page'] == page
    validate(instance=response.json(), schema=schema)


@allure.tag('api')
@allure.title('Получение количества пользователей на странице')
def test_users_list_default_length():
    default_users_count = 6
    schema = load_json_schema('get_users_list_default_length.json')

    response = reqres_session.get('/api/users')

    assert len(response.json()['data']) == default_users_count
    validate(instance=response.json(), schema=schema)


@allure.tag('api')
@allure.title('Поиск не существующего пользователя')
def test_single_user_not_found():
    response = reqres_session.get('/api/users/23')

    schema = load_json_schema('get_single_user_not_found.json')

    assert response.status_code == 404
    assert response.text == '{}'
    validate(instance=response.json(), schema=schema)


@allure.tag('api')
@allure.title('Создание пользователя')
def test_create_user():
    name = "jane"
    job = "job"

    schema = load_json_schema('post_create_user.json')

    response = reqres_session.post(
        url='/api/users',
        json={
            "name": name,
            "job": job}
    )

    assert response.status_code == 201
    assert response.json()['name'] == name
    validate(instance=response.json(), schema=schema)


@allure.tag('api')
@allure.title('Обновление пользователя')
def test_update_user():
    name = "Fill"
    job = "leader"

    schema = load_json_schema("put_update_user_schema.json")

    response = reqres_session.put("/api/users/23", json={"name": name, "job": job})

    assert response.status_code == 200
    assert response.json()["name"] == name
    validate(instance=response.json(), schema=schema)


@allure.tag('api')
@allure.title('Получение общего количества пользователей')
def test_requested_total_number():
    total = 12
    schema = load_json_schema("get_requested_total_number.json")

    response = reqres_session.get('/api/users', params={'total': total})

    assert response.status_code == 200
    assert response.json()['total'] == total
    validate(instance=response.json(), schema=schema)


@allure.tag('api')
@allure.title('Регистрация пользователя без пароля')
def test_register_user_error():
    response = reqres_session.post(
        url='/api/register',
        json={
            "email": "sydney@fife"
        }
    )
    schema = load_json_schema("post_register_user_error.json")

    assert response.status_code == 400
    assert response.text == '{"error":"Missing password"}'
    validate(instance=response.json(), schema=schema)


@allure.tag('api')
@allure.title('Успешная регистрация пользователя')
def test_registration_successful():
    token = 'QpwL5tke4Pnpja7X4'

    schema = load_json_schema("post_registration_successful.json")
    response = reqres_session.post(
        url='/api/register',
        json={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
    )

    assert response.status_code == 200
    assert response.json()['token'] == token
    validate(instance=response.json(), schema=schema)


@allure.tag('api')
@allure.title('Успешная авторизация пользователя')
def test_authorization_successful():
    schema = load_json_schema("post_authorization_successful.json")

    response = reqres_session.post(
        url='/api/login',
        json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )

    assert response.status_code == 200
    assert response.text == '{"token":"QpwL5tke4Pnpja7X4"}'
    validate(instance=response.json(), schema=schema)