import sys
import os
# number1 = sys.argv[1]
name= list(os.environ.items())

keys = list(element[0] for element in name)
print(keys)

# print(number1)

def calculate_avg(*args):
    return sum(args) / len(args)


print(calculate_avg(1, 2, 3, 4, 5))


# def find_max(*args):
#     return max(args)

def find_max(*args):
    max_number = 0
    for element in args:
        max_number = max(element, max_number)
    
    return max_number
        

print(find_max(9, 10, 7, 8, 9))