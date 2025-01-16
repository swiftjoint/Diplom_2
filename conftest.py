import pytest
import requests
import config_urls
import data


@pytest.fixture()
def create_user():
    create_user = requests.post(f'{config_urls.BASE_URL}/{config_urls.CREATE_USER}', data=data.DATA_USER)
    yield create_user
    token = create_user.json()['accessToken']
    requests.delete(f'{config_urls.BASE_URL}/{config_urls.INFO_USER}', headers={'Authorization': token})


@pytest.fixture()
def create_user_duplicate():
    create_user1 = requests.post(f'{config_urls.BASE_URL}/{config_urls.CREATE_USER}', data=data.DATA_USER)
    create_user2 = requests.post(f'{config_urls.BASE_URL}/{config_urls.CREATE_USER}', data=data.DATA_USER)
    token = None
    if create_user1.status_code == data.SUCCESS_STATUS_CODE:
        token = create_user1.json()['accessToken']
    yield create_user1, create_user2, token
    if token:
        requests.delete(f'{config_urls.BASE_URL}/{config_urls.INFO_USER}', headers={'Authorization': token})


@pytest.fixture()
def create_user_return_token():
    create_user = requests.post(f'{config_urls.BASE_URL}/{config_urls.CREATE_USER}', data=data.DATA_USER)
    token = create_user.json()['accessToken']
    yield token
    requests.delete(f'{config_urls.BASE_URL}/{config_urls.INFO_USER}', headers={'Authorization': token})
