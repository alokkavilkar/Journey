import json

dict = {}

with open('server.conf', 'r') as f:
    line = f.readline()

    while line:
        line = line.rstrip()
        if not line.startswith("#") and len(line) > 1:
            line = line.split('=')
            dict[line[0]] = line[1]
        line = f.readline()

print(dict)

# str = '{"name": "alok"}'
# dict = json.loads(str)
# print(dict)

# Define a list of dictionaries
list_of_dicts = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}
]

# Print the list of dictionaries
print(list_of_dicts)

import json


str = '{"name": "alok"}'
dict = json.loads(str)
print(dict)

# dumps -> input = dictionary returns string
# loads -> input string, retruns dict
# dump works only with with open
# load also



python_dict = {'name': 'alok', 'age': 30}
json_string = json.dumps(python_dict)
dict = json.loads(json_string)
print(json_string, dict)  


list_of_dicts = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}
]

with open('server-conf.json', 'w+') as f:
    json.dump(list_of_dicts, fp=f, indent=4)


with open('server-conf.json', 'w') as f:
    f.write(json.dumps(list_of_dicts))

str = '{"name": "alok"}'
dict = json.loads(str)
print(dict)

with open('server-conf.json', 'r') as f:
    doc = json.load(f)

print(doc)

with open('server-conf.json', 'w') as f:
    json.dump(list_of_dicts, f, indent=4)
