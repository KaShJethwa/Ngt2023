import json

#some JSON:
x = '{"name":"Karan","age":20,"city":"Mumbai"}'

# parse x:
y = json.loads(x)

#the result is the python directory
print(y["age"])
