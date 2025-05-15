from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Eve")
c2 = Customer("Mike")
latte = Coffee("Latte")
mocha = Coffee("Mocha")

o1 = c1.create_order(latte, 5.0)
o2 = c1.create_order(latte, 4.5)
o3 = c2.create_order(mocha, 6.0)
o4 = c2.create_order(latte, 6.5)

print("Latte num orders:", latte.num_orders())
print("Latte avg price:", latte.average_price())
print("Most aficionado for latte:", Customer.most_aficionado(latte).name)