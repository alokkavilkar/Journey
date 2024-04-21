my_dict = {
    "name": "Alok",
    "age":20,
    "programming_lanugages": ["python", 'JS', "GOLANG"],
    "is_married":False,
    "address":{
        "city":"Panvel",
        "residency_add":{
            "building_name":"Aradhya Residency",
            "room_no":303,
        }
    }
}

print(my_dict)
print(type(my_dict))
print(my_dict["name"])
my_dict["programming_lanugages"].append("Docker")
print(my_dict["programming_lanugages"])
# for key, _ in my_dict.items():
#     print(key, )

# Characteristics of Dictionaries:
# 1. Key value pair
# 2. mutable
# 3. Unordered
# 4. indexed
# 5. Cannot creates duplicates keys


# ----------------- Methods in dictionaries. ---------

print(type(my_dict.keys()))
print(my_dict.values())


list = [1, 2, 3, 4, 5, 4, 2, 3, 1, 7, 8]

count_map = {}

for element in list:
    # if count_map.get(element) != None:
    #     print(element , "is present")

    if count_map.__contains__(element):
        count = count_map.get(element)
        count_map[element] = count + 1
    else:
        count_map[element] = 1

print(count_map)

updateMap = {
    "organizationWork" : "amazon"
}

my_dict.update(updateMap)
print(my_dict)

# list3 = [1, 2, 3]
# list4 = [4, 5, 6]
# print(list3)
# list3.extend(list4)
# print(list3)

print(my_dict.get("Name")) # prints None and if uses slicing then it might leads to error

del my_dict["is_married"]

print(my_dict)

print(type(my_dict.items()))
