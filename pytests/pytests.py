import pytest

# pip install -U pytest
# Запускать с помощью "python -m pytest .\pytests.py"
# pytest Проверяет все функции, в названии которых стоит test_
# 1. Тестовая функция
def test_addition():
    assert 1 + 1 == 2

# 2. Несколько тестов одной функции
def add(a, b):
    return a + b

def test_add_function():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# 3. Тест на получение ошибок
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_function():
    with pytest.raises(ValueError):
        divide(5, 0)
    assert divide(6, 3) == 2

# 4. Параметризированый тест позволяет тестировать одну и ту же функцию с разными входными данными
@pytest.mark.parametrize("input, expected", [(1, 2), (2, 4), (3, 6)])
def test_multiply_by_two(input, expected):
    assert input * 2 == expected

# 5. Фикстура создаёт единый набор данных для всех тестов
@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_list_length(sample_list):
    assert len(sample_list) == 5

def test_list_sum(sample_list):
    assert sum(sample_list) == 15

# 6. Моки позволяют заменить сложные функции (Заранее указать им результат) и изолировать код
import requests
from unittest.mock import MagicMock, patch

def get_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def test_get_data_from_api():
    # Создание мока для функции requests.get
    mock_get = MagicMock()
    
    # Замена реальной функции requests.get моком в тесте
    with patch('requests.get', mock_get):
        # Установка поведения мока при вызове
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}
        mock_get.return_value = mock_response

        # Вызов тестируемой функции, которая будет использовать мок
        result = get_data_from_api('http://example.com/api')

    # Проверка взаимодействия с моком
    mock_get.assert_called_once_with('http://example.com/api')
    mock_response.json.assert_called_once()

    # Проверка результата функции
    assert result == {'key': 'value'}