# Coffee Shop Domain Model

## Overview
Object-oriented Python model of a coffee shop with `Customer`, `Coffee`, and `Order` entities. Relationships and behaviors between objects are modeled with proper validation and business logic.

## How to Run
```bash
pipenv install
pipenv shell
python debug.py
Tests
bash
Copy
Edit
pytest
Features
Input validation

Relationship modeling (many-to-many via Order)

Aggregate functions (average price, number of orders)

most_aficionado finder method

pgsql
Copy
Edit

---

### `tests/test_customer.py` (Example)

```python
import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")

    with pytest.raises(ValueError):
        Customer("A very long name exceeding 15")

    c = Customer("John")
    assert c.name == "John"

def test_customer_create_order():
    c = Customer("Mia")
    coffee = Coffee("Cappuccino")
    order = c.create_order(coffee, 5.0)
    assert order.customer == c
    assert order.coffee == coffee