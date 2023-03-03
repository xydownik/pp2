#Converts pyhton to JSON
import json

# a Python object (dict):
x = {
  "name": "Aruzhan",
  "age": 18,
  "city": "Esik"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None
print(json.dumps({"group" : "Americ anFootball", "year" : 1986}))
print(json.dumps(["Greta Van Fleet", "Red Hot Chili Peppers"]))
print(json.dumps(("Greta Van Fleet", "Red Hot Chili Peppers")))
print(json.dumps("Definitely maybe"))
print(json.dumps(15))
print(json.dumps(19.95))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#object with all the legal data types

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
print(json.dumps(x, indent = 4))  #formatting the results
print(json.dumps(x,indent =4, separators=(". "," = " ))) #changes the default sep
print(json.dumps(x, indent = 4, sort_keys= True)) #sorts the keys by alphabet