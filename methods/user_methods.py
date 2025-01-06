import allure
import requests
import config_urls


class UserMethods:
    @allure.step('Отправляем запрос, на создание пользователя без 1 обязательного поля')
    @allure.description('Запрос на ручку api/auth/register, данные статичные, хранятся в файле data')
    def create_user_without_required_field(self, auth_data):
        create_user = requests.post(f'{config_urls.BASE_URL}/{config_urls.CREATE_USER}', data=auth_data)
        return create_user

    @allure.step('Отправляем запрос, на авторизацию пользователя')
    @allure.description('Запрос на ручку api/auth/login, данные статичные, хранятся в файле data')
    def auth_user(self, auth_data):
        auth_user = requests.post(f'{config_urls.BASE_URL}/{config_urls.AUTH_USER}', data=auth_data)
        return auth_user

    @allure.step('Отправляем запрос, на обновление данных пользователя')
    @allure.description('Запрос на ручку api/auth/user, данные статичные, хранятся в файле data')
    def update_data_user_auth(self, auth_data, token):
        update_response = requests.patch(f'{config_urls.BASE_URL}/{config_urls.INFO_USER}', data=auth_data,
                                         headers={'Authorization': token})
        return update_response

    @allure.step('Отправляем запрос, на обновление данных пользователя без токена')
    @allure.description('Запрос на ручку api/auth/user, данные статичные, хранятся в файле data')
    def update_data_user_not_auth(self, auth_data):
        update_response = requests.patch(f'{config_urls.BASE_URL}/{config_urls.INFO_USER}', data=auth_data)
        return update_response
