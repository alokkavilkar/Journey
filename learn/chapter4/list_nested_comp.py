# Q.1 Generate a list of strings from a given list of strings where each string has more than 3 characters and starts with a vowel.
words = ['apple', 'banana', 'orange', 'kiwi', 'pear']

list_vowels = ['a', 'e', 'i', 'o', 'u']

result = [word for word in words if len(word) > 3 and all(word.startswith(vowels) for vowels in list_vowels)]

print(result)

# Q.2 Use nested list comprehension to filter out lists from a list of lists where all elements are positive integers.

matrix = [[1, 2, 3], [4, -5, 6], [7, 8, 9]]

result = [item for item in matrix if all(element > 0 for element in item)]
print(result)

# Q.3 Use nested list comprehension to filter out tuples from a list of tuples where the sum of their elements is greater than 10.

pairs = [(2, 3), (4, 6), (5, 4), (7, 1), (9, 2)]

result = [subitem for subitem in pairs if sum(subitem) >= 10]
print(result)


# Generate a list of sets from a list of sets where each set contains only unique elements.

sets = [{1, 2, 3}, {3, 4, 4}, {5, 6, 7}, {7, 8, 9}]

#  result = [subitem for subitem in sets if any()]


# Filter out rows from a matrix (list of lists) where the sum of elements in each row is greater than 20.

matrix = [[10, 5, 8], [3, 12, 6], [7, 9, 11], [4, 5, 6]]

result = [subitem for subitem in matrix if sum(subitem) >= 20]
print(result)
v = bin(3)
print(v[2:])

binary = [bin(x)[2:] for x in range(1, 11)]
print(binary)


