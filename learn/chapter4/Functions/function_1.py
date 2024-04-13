# Function Modules, packages 
# how to import packages 
# python workspace

# addition function

def add_fun(a, b, name):
    return f"Hello {name}, your sum is {a + b}"

 

# x = add_fun(10, 20, "Alok")
# print(x)

str = add_fun(10, 20, "Alok")
print(str)



# Module is group of functions
# my_module.py
# def square(x):
#     return x ** 2

# pi = 3.14159265

# import my_module

# result = my_module.square(5)
# print(result)
# print(my_module.pi)

'''
A package is a collection of modules organized in directories. Packages help you organize related modules into a hierarchy. They contain a special file named __init__.py, which indicates that the directory should be treated as a package.

Example:

Suppose you have a package structure as follows:

my_package/
    __init__.py
    module1.py
    module2.py
You can use modules from this package as follows:

from my_package import module1

result = module1.function_from_module1()

'''

import module as my_functions

x = my_functions.add(10, 2)

# or if we only import without alias then x = module.add(10, 20)
print(x)



