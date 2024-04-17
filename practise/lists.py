list1 = [element for element in range(1, 21)]
print(list1)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].encode('utf-8'))

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# del motorcycles[0]
# print(motorcycles)

# motorcycles.pop()
# print(motorcycles)
# motorcycles.pop()
# print(motorcycles)
motorcycles.pop(-2)
print(motorcycles)

somthing_in_return = motorcycles.remove('honda')
print(somthing_in_return)

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician, end=' ')


print(magician)


max_num = max(list1)
print(max_num)

words = ['apple', 'banana', 'orange', 'kiwi', 'pear']

vowels = ['a', 'e', 'i', 'o', 'u']

ans_list = [word for word in words if len(word) > 3 and any(word.startswith(vowel) for vowel in vowels)]


print(ans_list)

matrix = [[1, 2, 3], [4, -5, 6], [7, 8, 9]]

result = [item for item in matrix if all(element > 5 for element in item)]
print(result)

# Q.3 Use nested list comprehension to filter out tuples from a list of tuples where the sum of their elements is greater than 10.

pairs = [(2, 3), (4, 6), (5, 4), (7, 1), (9, 2)]

ans = [(a, b) for a, b in pairs if (a + b) > 10]
print(ans)


# Generate a list of sets from a list of sets where each set contains only unique elements.

sets = [[1, 2, 3], [4, 5, 4], [7, 7, 8], [10, 9, 10, 10]]

# x = [True, False, True]

# print(any(x))
ans = [element for element in sets if all(not element.count(item) > 1 for item in element)]
print(ans)



print(sets[:])
# print(sets[:,1:])

import numpy as np

array = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8],
                  [6, 7, 6]])

print(array[::2]) #same as arra[..., 2]
# print(array[1:3])
# print(array[1,2:])
# print(array[::,2:])
# print(array[1:3, 1:3])  row chi kiti slicing karaychi and column chi kiti
# print(array[1:, 2:])
print(array[:2])
# print(array[::2, 2:])


dict = {"name":"Alok", "age":"20"}
# new_dict = dict.fromkeys(dict)
# dict.
# print(new_dict)

def function_arg(*args):
    for element in args:
        print(element)


function_arg((10, 20, 30, 50, 60))

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    # for key, value in user_info.items():
    #     profile[key] = value
    print(type(user_info))
    return profile


user_profile = build_profile('albert', 'einstein',location='princeton', field='physics')
print(user_profile)
