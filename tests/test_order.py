import allure
import data
from methods.order_methods import OrderMethods


class TestOrder:
    @allure.title('Проверяем создание заказа, авторизованный с ингредиентами, ожидаем статус-код 200')
    def test_create_order_auth_with_ingredients(self, create_user_return_token):
        token = create_user_return_token
        order_methods = OrderMethods()
        response = order_methods.create_order_auth(data.VALID_DATA_INGREDIENTS, token)
        response_body = response.json()

        assert (
                response.status_code == data.SUCCESS_STATUS_CODE and
                response_body.get("success") == data.EXPECTED_CREATE_ORDER_RESPONSE_TRUE["success"]
        ), (f'Ожидались статус-код 200 и success: true, но пришло статус-код {response.status_code} '
            f'и ответ {response_body}')

    @allure.title('Проверяем создание заказа, авторизованный без ингредиентов, ожидаем статус-код 400')
    def test_create_order_auth_without_ingredients(self, create_user_return_token):
        token = create_user_return_token
        order_methods = OrderMethods()
        response = order_methods.create_order_auth(data.WITHOUT_DATA_INGREDIENTS, token)
        response_body = response.json()

        assert (
                response.status_code == data.BAD_REQUEST and
                response_body.get("success") == data.EXPECTED_CREATE_ORDER_RESPONSE_FALSE["success"]
        ), (f'Ожидались статус-код 200 и success: false, но пришло статус-код {response.status_code} '
            f'и ответ {response_body}')

    @allure.title('Проверяем создание заказа, неавторизованный с ингредиентами, ожидаем статус-код 403')
    def test_create_order_not_auth_with_ingredients(self,  create_user):
        order_methods = OrderMethods()
        response = order_methods.create_order_not_auth(data.VALID_DATA_INGREDIENTS)
        response_body = response.json()

        assert (
                response.status_code == data.SUCCESS_STATUS_CODE and
                response_body.get("success") == data.EXPECTED_CREATE_ORDER_RESPONSE_TRUE["success"]
        ), (f'Ожидались статус-код 403 и success: false, но пришло статус-код {response.status_code} '
            f'и ответ {response_body}')

    @allure.title('Проверяем создание заказа, авторизованный с неверным хешам ингредиента, ожидаем статус-код 500')
    def test_create_order_auth_invalid_hash_ingredients(self, create_user_return_token):
        token = create_user_return_token
        order_methods = OrderMethods()
        response = order_methods.create_order_auth(data.INVALID_DATA_INGREDIENTS, token)
        response_body = response.text

        assert (
                response.status_code == data.INTERNAL_SERVER_ERROR and data.EXPECTED_ERROR_TEXT in response_body
        ), (f'Ожидались статус-код 500 и текст "{data.EXPECTED_ERROR_TEXT}", '
            f'но пришло статус-код {response.status_code} и текст {response_body}')

    @allure.title('Проверяем получение списка заказа, авторизованный, ожидаем статус-код 200')
    def test_get_orders_auth_user(self, create_user_return_token):
        token = create_user_return_token
        get_order_methods = OrderMethods()
        response = get_order_methods.get_orders_auth_user(token)
        response_body = response.json()

        assert (
                response.status_code == data.SUCCESS_STATUS_CODE and
                response_body.get("success") == data.EXPECTED_CREATE_ORDER_RESPONSE_TRUE["success"]
        ), (f'Ожидались статус-код 200 и success: true, но пришло статус-код {response.status_code} '
            f'и ответ {response_body}')

    @allure.title('Проверяем получение списка заказа, неавторизованный, ожидаем статус-код 401')
    def test_get_orders_not_auth_user(self):
        get_order_methods = OrderMethods()
        response = get_order_methods.get_orders_not_auth_user()
        response_body = response.json()

        assert (
                response.status_code == data.UNAUTHORIZED_STATUS_CODE and
                response_body.get("success") == data.EXPECTED_CREATE_ORDER_RESPONSE_FALSE["success"]
        ), (f'Ожидались статус-код 401 и success: false, но пришло статус-код {response.status_code} '
            f'и ответ {response_body}')
