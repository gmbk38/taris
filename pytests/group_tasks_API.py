import requests
import pytest
from unittest.mock import patch

URL = 'https://api.github.com/users/gmbk38'

def get_data():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()


def get_attribute(atr):
    return get_data()[atr]

# Обычный тест
def test_get_data():
    assert isinstance(get_data(), dict)

# Тест на получение ошибки
def test_get_data_2():
    with pytest.raises(KeyError):
        get_attribute('sum')
    get_attribute('login')

# Несколько данных для одной функции
@pytest.mark.parametrize("input, expected", [(get_data()['login'], 'gmbk38'), (get_data()['id'], 79657946), (get_data()['name'], 'Kirillov Dmitrii')])
def test_get_data_3(input, expected):
    assert input == expected

# Фикстура. В ней делаем один запрос по API и передаём в тесты в качестве параметра
@pytest.fixture
def get_data_fixture():
    return get_data()

def test_list(get_data_fixture):
    with pytest.raises(KeyError):
        get_data_fixture['sum']

def test_list_2(get_data_fixture):
    assert isinstance(get_data_fixture, dict)

# Мок, который заменяет содержимое JSON для упрощения тестирования
def test_get_data_4():
    # Используем контекстный менеджер patch для временной замены response.json
    with patch('requests.get') as mock_get:
        # Создаем мок-объект для возвращения нужного значения
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'sum': 100}
        # Теперь функция get_data будет использовать мок requests.get
        data = get_data()
        # Проверим, что возвращенный результат соответствует ожидаемому
        assert data == {'sum': 100}