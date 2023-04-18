EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    },
    {
        "id": 2,
        "name": "Patrick Lunas"
    }
]


def get_all_employees():
    """gets all employees
    """
    return EMPLOYEES


def get_single_employee(id):
    """gets a single employee based off of the ID
    """
    requested_employee = None

    for employee in EMPLOYEES:
        if employee['id'] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    """creates a new employee
    """
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee
