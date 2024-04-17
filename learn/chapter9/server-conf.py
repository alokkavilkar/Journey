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


with open('server-conf.json', 'w') as f:
    json.dump(list_of_dicts, f, indent=4)