import requests
import pytest

URL = 'https://api.github.com/users/gmbk38'

def get_data():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()

def test_get_data():
    assert isinstance(get_data(), dict)
