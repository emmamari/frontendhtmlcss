import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import hw_api_tests.employees_api_end_points as emp
import hw_api_tests.checker as checker


def test_employees_api():
    # GET ALL
    response = emp.get_all_employees()
    checker.check_status_code(response, 200)
    checker.check_data_type(response, list)

    # POST
    json_to_create_employee = {
        "name": "Ivan",
        "surname": "Ivanov",
        "salary": 1000,
        "department": "HR"
    }
    response = emp.create_employee(json_to_create_employee)
    checker.check_status_code(response, 200)

    created_employee = response.json()
    for k, v in json_to_create_employee.items():
        checker.check_value(response, k, v)

    # POST 400
    json_to_create_employee_invalid = {
        "Name": "Ivan",
        "srname": "Ivanov",
        "salary": 1000,
        "department": "HR"
    }
    response = emp.create_employee(json_to_create_employee_invalid)
    checker.check_status_code(response, 400)

    # GET ID
    employee_id = created_employee['id']
    response = emp.get_employee_by_id(employee_id)
    checker.check_status_code(response, 200)

    # PUT
    json_to_update_employee = {
        "id": employee_id,
        "name": "Ivan",
        "surname": "Ivanov",
        "salary": 3100,
        "department": "Sales"
    }
    response = emp.update_employee(json_to_update_employee)
    checker.check_status_code(response, 200)
    updated_employee = response.json()
    for k, v in updated_employee.items():
        checker.check_value(response, k, v)

    # PUT 400
    json_to_update_employee_invalid  = {
        "name": "hgdg",
        "hh":445,
        "surname": "False",
    }
    response = emp.update_employee(json_to_update_employee_invalid)
    checker.check_status_code(response, 400)

    # PUT 403
    json_to_update_forbidden_employee = {
        "id": 99,
        "name": "Ivan",
        "surname": "Ivanov",
        "salary": 3100,
        "department": "Sales"
    }
    forbidden_employee_id = 85
    response = emp.update_employee(json_to_update_forbidden_employee)
    checker.check_status_code(response, 403)

    # PUT 404
    json_to_update_forbidden_non_existent_employee = {
        "id": 101,
        "name": "Ivan",
        "surname": "Ivanov",
        "salary": 3100,
        "department": "Sales"
    }

    response = emp.update_employee(json_to_update_forbidden_non_existent_employee)
    checker.check_status_code(response, 404)

    # DELETE
    response = emp.delete_employee(employee_id)
    checker.check_status_code(response, 200)

    # DELETE 404
    response = emp.delete_employee(employee_id)
    checker.check_status_code(response, 404)

    #id<=100 403
    response = emp.delete_employee(forbidden_employee_id)
    checker.check_status_code(response, 403)

    #GET ID NONE 404
    non_existent_employee_id = 101
    response = emp.get_employee_by_id(non_existent_employee_id)
    checker.check_status_code(response, 404)