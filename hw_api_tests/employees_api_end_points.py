import requests

base_url = 'https://emps.alatoo.edu.kg'
headers = {'Content-type': 'application/json',
          'Authorization': 'Bearer d98f025c603ddbc0b8da57e9f18acc3dd030df063def72874b3b23c7baaf7bf3'}

#GET ALL
def get_all_employees():
    url = base_url + '/api/employees'
    print('\nGET ALL USERS')
    print('URL: ', url)
    response = requests.get(url, headers=headers)
    elements_list = response.json()
    for i in range(5):
        print(elements_list[i])
        if i == len(elements_list) - 1:
            break
    return response

# POST
def create_employee(employee_data):
    url = base_url + '/api/employees'
    print('\nPOST')
    print('URL: ', url)
    response = requests.post(url, json=employee_data, headers=headers)
    print(response.text)
    return response

# GET BY ID
def get_employee_by_id(employee_id):
    url = base_url + '/api/employees' + '/' + str(employee_id)
    print('\nGET ID')
    print('URL: ', url)
    response = requests.get(url, headers=headers)
    print(response.text)
    return response

# PUT UPDATE
def update_employee(updated_data):
    url = base_url + '/api/employees'# + '/' + str(employee_id)
    print('\nPUT')
    print('URL: ', url)
    response = requests.put(url, json=updated_data, headers=headers)
    print(response.text)
    return response

#DELETE
def  delete_employee(employee_id):
    url = base_url + '/api/employees' + '/' + str(employee_id)
    print('\nDELETE')
    print('URL: ', url)
    response = requests.delete(url, headers=headers)
    return response