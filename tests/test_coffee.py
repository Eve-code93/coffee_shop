def test_num_orders_and_average_price():
    from customer import Customer
    from coffee import Coffee
    from order import Order

    Order.all.clear()
    c = Customer("Alex")
    coffee = Coffee("Espresso")
    c.create_order(coffee, 3.0)
    c.create_order(coffee, 6.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.5
