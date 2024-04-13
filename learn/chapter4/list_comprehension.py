squares = [x ** 2 for x in range(1, 11)]
print(squares)

# matrix = [[x*y for y in range(1, 4)] for x in range(1, 4)]
# working in below behind the scene

matrix = []
for y in range(1, 4):
    new_list = []
    for x in range(1, 4):
        new_list.append(x * y)
    matrix.append(new_list)
    
print(matrix)

words = ["alok", "kavilkar"]
upper_words = [word.upper() for word in words]
print(upper_words)

tuples = [(1, 2), (3, 4), (5, 6)]
flattened = [item for items in tuples for item in items]
print(flattened)


# Questions to practise.



# Given the list of numbers [2, 3, 5, 7, 8, 11, 13, 17, 19], create a new list containing only the prime numbers.

list = [2, 3, 5, 7, 8, 11, 13, 17, 19]
prime_list = [item for item in list if all(item % i != 0 for i in range(2, item))]
print(prime_list)

# Given the list of strings ['apple', 'banana', 'orange', 'watermelon', 'kiwi'], create a new list containing only the strings with more than 5 characters.
fruits = ['apple', 'banana', 'orange', 'watermelon', 'kiwi']
filter = [fruit for fruit in fruits if len(fruit) > 5]
print(filter)

# Given the 2D list (matrix) [[1, 2, 3], [4, 5, 6], [7, 8, 9]], create a flattened list containing all elements of the matrix.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattenedList = [value for x in matrix for value in x]
print(flattenedList)


# Given the list of tuples [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')], create a new list containing the second element of each tuple.

list_tuple = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
new_list = [x[1] for x in list_tuple ]
print(new_list)

# Generate a list of Fibonacci numbers less than 1000.
# list_fib = [x for ]


# Given the list of integers [-3, 7, -5, 2, 0, -9, 6], create a new list containing the absolute values of all elements.

list = [-3, 7, -5, 2, 0, -9, 6]
new_list_abs = [abs(val) for val in list]
print(new_list_abs)


# Define the maximum value for a and b
max_value = 10

# Create a list of tuples where each tuple contains two integers (a, b) such that a divides b evenly
result = [[a,b] for a in range(1, max_value) for b in range(a, max_value) if b % a == 0]

# Print the list of tuples
print(result)


# Generate a list of squares of even numbers and cubes of odd numbers less than 20.

# Generate a list of squares of even numbers and cubes of odd numbers less than 20.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x ** 2 if x % 2 == 0 else x ** 3 for x in numbers if x < 20]
print(result)
