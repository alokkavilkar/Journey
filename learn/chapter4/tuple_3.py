# Question: Write a Python expression to create a tuple containing the squares of numbers from 1 to 5.

q = (1, 2, 3, 4, 5)
result = tuple(element ** 2 for element in q)
print(result)

# Question: Create a tuple containing the lengths of strings from a given tuple of strings.

q = ("apple", "banana", "kiwi", "strawberry")
result = tuple(len(word) for word in q)
print(result)

# Question: Write a Python expression to create a tuple containing only the even numbers from a given tuple of integers.

q = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = (even_numbers for elements in q if elements )


# Given the list of numbers [2, 3, 5, 7, 8, 11, 13, 17, 19], create a new list containing only the prime numbers.
numbers = [2, 3, 5, 7, 8, 11, 13, 17, 19]
prime_list = [item for item in numbers if all(item % i != 0 for i in range(2, item))]
print(prime_list)

# Generate a list of squares of even numbers and cubes of odd numbers less than 20.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x ** 2 if x % 2 == 0 else x ** 3 for x in numbers if x < 20]
print(result)


