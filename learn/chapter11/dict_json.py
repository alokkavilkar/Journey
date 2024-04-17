import json

server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', "Server not found")

server_name = 'server7'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")

sample_json = {
    "server1":{
        "status":"online",
        "ip":"192.168.1.1"
    },
    "server2":{
        "status":"offline",
        "ip":"192.168.1.2"
    }
}

json_object_str = '''{
    "server1":{
        "status":"online",
        "ip":"192.168.1.1"
    },
    "server2":{
        "status":"offline",
        "ip":"192.168.1.2"
    }
}'''

print(type(json_object_str))
data = json.loads(json_object_str)
print(data)
with open('sample2.json', 'w') as f:
    f.write(json.dumps(json_object_str))

print(type(sample_json))

with open('server.json', 'w') as f:
    json.dump(sample_json, f, indent=4)


with open('server.json', 'r') as f:
    dict = json.load(f)


print(dict['server1']['ip'])



# Given the sample JSON object, how would you access the IP address of 'server1'?

with open('server.json', 'r') as f:
    data = json.load(f)

# print(type(data))
print(data['server1']['ip'])
data.update({"server:3": {"status": "online", "ip": "192.168.1.3"}})

with open('server.json', 'w') as f:
    json.dump(data, f, indent=4)

print(data)

def get_server_status(data, server_name):
    return 1, 0

x, y =  get_server_status('10', 20)
print(x, y)