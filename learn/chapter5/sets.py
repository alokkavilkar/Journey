# Sets are dictionaries type without values
# cannot add list as list is mutable but can add tuple
# my_set = {1, 2, 3, "True", [1, 2, 3]}
my_set = {1, 2, 3, (1, 2, 3)}
print(my_set)
my_set.add(1)
print(my_set)
my_set.remove((1, 2, 3))
print(my_set)


# but in tuple adding list is does;nt give error

t = (1, 2, "string", [1, 2, 3])
t[3].append(10)
print(t)

# creates empty set
new_s = {}
print(type(new_s))
s = set()
print(type(s))

print(my_set)
my_set.pop()
print(my_set)
my_set.pop()
print(my_set)
my_set.add(10)
print(my_set)
my_set.add(20)
print(my_set)

