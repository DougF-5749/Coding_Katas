import json

# Convert a JSON string like the one below to a Python dictionary and returns the product name and price
# JSON string = '{"product": "Laptop", "price": 1200, "available": true}'

def return_name_and_price(json_string):
    # convert json_string into python dictionary
    python_dict = json.loads(json_string)

    # return new dictionary containingn price and product name
    return {k:v for (k,v) in python_dict.items() if k != "available"}

# Convert Python dictionary back to JSON string

def dict_to_json_string(dictionary):
    return json.dumps(dictionary)