def check_status_code(response, expected_status_code):
    print(f'Status code: {response.status_code}')
    assert response.status_code == expected_status_code
    print(f'Status code верный!')

def check_data_type(response, expected_data_type):
    assert expected_data_type == type(response.json())
    print(f'Тип данных верный!')

def check_value(response, key, expected_value):
    response_dict = response.json()
    assert expected_value == response_dict.get(key)
    print(f'Значение по ключу {key} верно!')