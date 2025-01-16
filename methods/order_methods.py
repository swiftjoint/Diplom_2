import allure
import requests
import config_urls


class OrderMethods:
    @allure.step('Отправляем запрос, на создание заказа авторизованный')
    @allure.description('Запрос на ручку api/orders, данные статичные, хранятся в файле data')
    def create_order_auth(self, order_data, token):
        create_order_auth = requests.post(f'{config_urls.BASE_URL}/{config_urls.INFO_ORDER}',
                                          data=order_data, headers={'Authorization': token})
        return create_order_auth

    @allure.step('Отправляем запрос, на создание заказа неавторизованный')
    @allure.description('Запрос на ручку api/orders, данные статичные, хранятся в файле data')
    def create_order_not_auth(self, order_data):
        create_order_auth = requests.post(f'{config_urls.BASE_URL}/{config_urls.INFO_ORDER}', data=order_data,)
        return create_order_auth

    @allure.step('Отправляем запрос, на получение списка заказа конкретного пользователя, авторизованный')
    @allure.description('Запрос на ручку api/orders, данные статичные, хранятся в файле data')
    def get_orders_auth_user(self, token):
        get_orders = requests.get(f'{config_urls.BASE_URL}/{config_urls.INFO_ORDER}', headers={'Authorization': token})
        return get_orders

    @allure.step('Отправляем запрос, на получение списка заказа, неавторизованный')
    @allure.description('Запрос на ручку api/orders, данные статичные, хранятся в файле data')
    def get_orders_not_auth_user(self):
        get_orders = requests.get(f'{config_urls.BASE_URL}/{config_urls.INFO_ORDER}')
        return get_orders
