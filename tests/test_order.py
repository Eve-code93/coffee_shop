def test_order_validation():
    from customer import Customer
    from coffee import Coffee
    from order import Order
    import pytest

    c = Customer("Anna")
    coffee = Coffee("Mocha")

    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)  # price too low