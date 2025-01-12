allure_report
Содержит файл index.html, который представляет собой отчет о тестах в виде веб-сайта.

allure_results
Содержит файлы JSON, созданные Allure при прогонке тестов.

methods
Содержит файлы с методами для взаимодействия с API:

__init__.py: Инициализационный файл.

order_methods.py: Методы для работы с заказами.

create_order_auth(self, order_data, token): Отправляет запрос на создание заказа авторизованным пользователем.
create_order_not_auth(self, order_data): Отправляет запрос на создание заказа неавторизованным пользователем.
get_orders_auth_user(self, token): Отправляет запрос на получение списка заказов авторизованного пользователя.
get_orders_not_auth_user(self): Отправляет запрос на получение списка заказов неавторизованным пользователем.

user_methods.py: Методы для работы с пользователями.

create_user_without_required_field(self, auth_data): Отправляет запрос на создание пользователя без одного обязательного поля.
auth_user(self, auth_data): Отправляет запрос на авторизацию пользователя.
update_data_user_auth(self, auth_data, token): Отправляет запрос на обновление данных пользователя авторизованным пользователем.
update_data_user_not_auth(self, auth_data): Отправляет запрос на обновление данных пользователя неавторизованным пользователем.

tests
Содержит файлы с тестовыми методами:

test_order.py: Тесты для заказов.

test_create_order_auth_with_ingredients(self, create_user_return_token): Проверяет создание заказа авторизованным пользователем с ингредиентами, ожидает статус-код 200.
test_create_order_auth_without_ingredients(self, create_user_return_token): Проверяет создание заказа авторизованным пользователем без ингредиентов, ожидает статус-код 400.
test_create_order_not_auth_with_ingredients(self, create_user): Проверяет создание заказа неавторизованным пользователем с ингредиентами, ожидает статус-код 403.
test_create_order_auth_invalid_hash_ingredients(self, create_user_return_token): Проверяет создание заказа авторизованным пользователем с неверным хешем ингредиента, ожидает статус-код 500.
test_get_orders_auth_user(self, create_user_return_token): Проверяет получение списка заказов авторизованным пользователем, ожидает статус-код 200.
test_get_orders_not_auth_user(self): Проверяет получение списка заказов неавторизованным пользователем, ожидает статус-код 401.

test_user.py: Тесты для пользователей.

test_create_user_success(self, create_user): Проверяет успешное создание пользователя, ожидает статус-код 200.
test_user_create_duplicate(self, create_user_duplicate): Проверяет создание двух одинаковых пользователей, ожидает статус-код 403.
test_user_create_without_required_field(self, auth_data): Проверяет создание пользователя без одного обязательного поля, ожидает статус-код 403.
test_auth_success_user(self, create_user): Проверяет авторизацию созданного пользователя, ожидает статус-код 200.
test_auth_user_invalid_login_password(self, create_user, auth_data): Проверяет авторизацию созданного пользователя с неверным логином и паролем, ожидает статус-код 401.
test_update_user_auth(self, auth_data, create_user_return_token): Проверяет обновление данных пользователя (email и name) авторизованным пользователем, ожидает статус-код 200.
test_update_user_not_auth(self, auth_data, create_user): Проверяет обновление данных неавторизованного пользователя (email и name), ожидает статус-код 401.

config_urls.py
Содержит URL-адреса для различных API-запросов:

BASE_URL: Базовый URL.
CREATE_USER: URL для создания пользователя.
AUTH_USER: URL для авторизации пользователя.
INFO_USER: URL для получения информации о пользователе.
INFO_ORDER: URL для работы с заказами.

conftest.py
Содержит фикстуры для pytest:

create_user(): Фикстура для создания пользователя и удаления его после теста.
create_user_duplicate(): Фикстура для создания двух одинаковых пользователей и удаления их после теста.
create_user_return_token(): Фикстура для создания пользователя и возврата токена, с последующим удалением пользователя.

data.py
Содержит данные и константы для тестов:

DATA_USER: Данные для создания пользователя.
DATA_USER_WITHOUT_REQUIRED_FIELD: Данные для создания пользователя без одного обязательного поля.
DATA_AUTH_USER: Данные для авторизации пользователя.
DATA_AUTH_USERS_INVALID_LOGIN_PASSWORD: Данные для авторизации пользователя с неверным логином и паролем.
UPDATE_DATA_USER_AUTH: Данные для обновления данных пользователя авторизованным пользователем.
UPDATE_DATA_USER_NOT_AUTH: Данные для обновления данных пользователя неавторизованным пользователем.
VALID_DATA_INGREDIENTS: Данные для создания заказа с валидными ингредиентами.
WITHOUT_DATA_INGREDIENTS: Данные для создания заказа без ингредиентов.
INVALID_DATA_INGREDIENTS: Данные для создания заказа с неверными ингредиентами.
SUCCESS_STATUS_CODE: Статус-код успешного запроса.
FORBIDDEN_STATUS_CODE: Статус-код запрещенного запроса.
UNAUTHORIZED_STATUS_CODE: Статус-код неавторизованного запроса.
BAD_REQUEST: Статус-код неверного запроса.
INTERNAL_SERVER_ERROR: Статус-код внутренней ошибки сервера.
EXPECTED_CREATE_ORDER_RESPONSE_TRUE: Ожидаемый ответ на успешное создание заказа.
EXPECTED_CREATE_ORDER_RESPONSE_FALSE: Ожидаемый ответ на неуспешное создание заказа.
EXPECTED_ERROR_TEXT: Ожидаемый текст ошибки.

requirements.txt
Содержит список зависимостей проекта.
