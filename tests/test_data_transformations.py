from katas.data_transformations import *

# Convert a JSON string like the one below to a Python dictionary and returns the product name and price
# JSON string = '{"product": "Laptop", "price": 1200, "available": true}'

def test_return_name_and_price():
    json_string = '{"product": "Laptop", "price": 1200, "available": true}'
    actual = return_name_and_price(json_string)
    expected = {
        "price": 1200,
        "product": "Laptop"
    }

    assert actual == expected