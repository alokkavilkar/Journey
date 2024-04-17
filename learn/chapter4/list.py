# List is collection of different types of data values.
'''
list is collection of different types of value
changable
in give take format
'''
list = [1, 2, 3, 4, 5]
print(list)
print(list[::-1])
# list is changable
list[4] = 98

print(list)

# Different values of data
new_list = ["Alok", 21, "DevOps Engineer.", 39.0, False]
new_list.append("Alok")
print(new_list)
new_list[5] = [1, 2, 4]
print(new_list)
print(new_list[5][0])



new_list.extend([1, 2, 3])
print(new_list)
another_list = new_list.copy()
print(another_list)
x = new_list.pop(1) # remove and return the value;
y = new_list.remove(1) # remove the value;

print(new_list, y)
another_list.clear()
print(another_list)
