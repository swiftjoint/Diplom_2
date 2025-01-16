import allure
import pytest
import data
from methods.user_methods import UserMethods


class TestUser:
    @allure.title('Проверяем успешное создание пользователя, ожидаем статус-код 200')
    def test_create_user_success(self, create_user):
        response_body = create_user.json()

        assert (
                create_user.status_code == data.SUCCESS_STATUS_CODE and
                response_body.get("success") == data.EXPECTED_CREATE_ORDER_RESPONSE_TRUE["success"]
        ), (f'Ожидались статус-код 200 и success: true, но пришло статус-код {create_user.status_code} '
            f'и ответ {response_body}')

    @allure.title('Проверяем создание 2х одинаковых пользователей, ожидаем статус-код 403')
    def test_user_create_duplicate(self, create_user_duplicate):
        create_user1, create_user2, token = create_user_duplicate
        response_body = create_user2.json()

        assert (
                create_user2.status_code == data.FORBIDDEN_STATUS_CODE and
                response_body.get("success") == data.EXPECTED_CREATE_ORDER_RESPONSE_FALSE["success"]
        ), (f'Ожидался статус-код 403 и success: false, но пришло статус-код {create_user2.status_code} '
            f'и ответ {response_body}')

    @allure.title('Проверяем создание пользователя без 1 обязательного поля, ожидаем статус-код 403')
    @pytest.mark.parametrize('auth_data', data.DATA_USER_WITHOUT_REQUIRED_FIELD)
    def test_user_create_without_required_field(self, auth_data):
        user_methods = UserMethods()
        response = user_methods.create_user_without_required_field(auth_data)
        response_body = response.json()

        assert (
                response.status_code == data.FORBIDDEN_STATUS_CODE and
                response_body.get("success") == data.EXPECTED_CREATE_ORDER_RESPONSE_FALSE["success"]
        ), (f'Ожидался статус-код 403 и success: false, но пришло статус-код {response.status_code} '
            f'и ответ {response_body}')

    @allure.title('Проверяем авторизацию созданного пользователя, ожидаем статус-код 200')
    def test_auth_success_user(self, create_user):
        user_methods = UserMethods()
        auth_user = user_methods.auth_user(data.DATA_AUTH_USER)
        response_body = auth_user.json()

        assert (
                create_user.status_code == data.SUCCESS_STATUS_CODE and
                response_body.get("success") == data.EXPECTED_CREATE_ORDER_RESPONSE_TRUE["success"]
        ), (f'Ожидались статус-код 200 и success: true, но пришло статус-код {create_user.status_code} '
            f'и ответ {response_body}')

    @allure.title('Проверяем авторизацию созданного полььзователя, с неверным логином и '
                  'паролем, ожидаем статус-код 401')
    @pytest.mark.parametrize('auth_data', data.DATA_AUTH_USERS_INVALID_LOGIN_PASSWORD)
    def test_auth_user_invalid_login_password(self, create_user, auth_data):
        user_methods = UserMethods()
        response = user_methods.auth_user(auth_data)
        response_body = response.json()

        assert (
                response.status_code == data.UNAUTHORIZED_STATUS_CODE and
                response_body.get("success") == data.EXPECTED_CREATE_ORDER_RESPONSE_FALSE["success"]
        ), (f'Ожидался статус-код 403 и success: false, но пришло статус-код {response.status_code} '
            f'и ответ {response_body}')

    @allure.title('Проверяем обновление данных пользователя, email и name, ожидаем статус-код 200')
    @pytest.mark.parametrize('auth_data', data.UPDATE_DATA_USER_AUTH)
    def test_update_user_auth(self, auth_data, create_user_return_token):
        token = create_user_return_token
        user_methods = UserMethods()
        response = user_methods.update_data_user_auth(auth_data, token)
        response_body = response.json()

        assert (
                response.status_code == data.SUCCESS_STATUS_CODE and
                response_body.get("success") == data.EXPECTED_CREATE_ORDER_RESPONSE_TRUE["success"]
        ), (f'Ожидались статус-код 200 и success: true, но пришло статус-код {response.status_code} '
            f'и ответ {response_body}')

    @allure.title('Проверяем обновление данных неавторизованного пользователя, email и name, ожидаем статус-код 401')
    @pytest.mark.parametrize('auth_data', data.UPDATE_DATA_USER_NOT_AUTH)
    def test_update_user_not_auth(self, auth_data, create_user):
        user_methods = UserMethods()
        response = user_methods.update_data_user_not_auth(auth_data)
        response_body = response.json()

        assert (
                response.status_code == data.UNAUTHORIZED_STATUS_CODE and
                response_body.get("success") == data.EXPECTED_CREATE_ORDER_RESPONSE_FALSE["success"]
        ), (f'Ожидался статус-код 403 и success: false, но пришло статус-код {response.status_code} '
            f'и ответ {response_body}')
