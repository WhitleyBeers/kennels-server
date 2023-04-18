CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]


def get_all_customers():
    """
    gets all customers
    """
    return CUSTOMERS


def get_single_customer(id):
    """
    gets a customer by its id
    """
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
