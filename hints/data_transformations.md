You often convert between JSON and Python dictionaries using:

``` python 
import json

# JSON string --> python dictionary
data = json.loads('{"name": "Alice", "age": 30}')

# python dictionary --> JSON string
json_string = json.dumps(data)
```

This is the general template you can follow for dictionary comprehension in Python:

```python
dict_variable = {key:value for (key,value) in dictonary.items()}
``` 


