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
