DATA_USER = {
    'email': 'test-datatest@mail.ru',
    'password': 'Qwe123',
    'name': 'Хорхе'
}

DATA_USER_WITHOUT_REQUIRED_FIELD = [
    {'email': '', 'password': 'Qwe123', 'name': 'Хорхе'},
    {'email': 'test-datatest@mail.ru', 'password': '', 'name': 'Хорхе'},
    {'email': 'test-datatest@mail.ru', 'password': 'Qwe123', 'name': ''},
]

DATA_AUTH_USER = {
    'email': 'test-datatest@mail.ru',
    'password': 'Qwe123'
}

DATA_AUTH_USERS_INVALID_LOGIN_PASSWORD = [
    {'email': 'test-datatest1@mail.ru', 'password': '123Qwe'},
    {'email': 'datatest2@mail.ru', 'password': 'Qwe123'},
]

UPDATE_DATA_USER_AUTH = [
    {'email': 'datatestdata@mail.ru', 'name': 'Хорхе'},
    {'email': 'datatestdata@mail.ru', 'name': 'Хорхе1'},
]

UPDATE_DATA_USER_NOT_AUTH = [
    {'email': 'test-datatest@mail.ru', 'name': 'Хорхе1'},
    {'email': 'datatestdata@mail.ru', 'name': 'Хорхе'},
]

VALID_DATA_INGREDIENTS = {
    'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']
}

WITHOUT_DATA_INGREDIENTS = {
    'ingredients': []
}

INVALID_DATA_INGREDIENTS = {
    'ingredients': ['61c0c5a71dfbfb84854181', 'efefgrfrv484v51v8r45e9fegx']
}

SUCCESS_STATUS_CODE = 200
FORBIDDEN_STATUS_CODE = 403
UNAUTHORIZED_STATUS_CODE = 401
BAD_REQUEST = 400
INTERNAL_SERVER_ERROR = 500

EXPECTED_CREATE_ORDER_RESPONSE_TRUE = {
    "success": True
}

EXPECTED_CREATE_ORDER_RESPONSE_FALSE = {
    "success": False
}

EXPECTED_ERROR_TEXT = "Internal Server Error"
