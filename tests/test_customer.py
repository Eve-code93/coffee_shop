import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_create_order():
    c = Customer("Mbithe")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 5.0)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 5.0


def test_invalid_name():
    with pytest.raises(ValueError):
        Customer("A" * 20)
