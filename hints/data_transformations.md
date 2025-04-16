You often convert between JSON and Python dictionaries using:

``` python 
import json

# JSON string --> python dictionary
data = json.loads('{"name": "Alice", "age": 30}')

# python dictionary --> JSON string
json_string = json.dumps(data)
```

