#convert from JSON to Python -> Parse JSON
import json
x = '{"name" : "Aruzhan", "age" : 18, "city" : "Esik"}' #example json
y = json.loads(x)  #Parse x
print(y["city"])


