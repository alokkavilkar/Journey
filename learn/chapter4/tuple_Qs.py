# 1. Write a Python function that takes two tuples as input and returns a new tuple containing the elements that are common to both input tuples.

# input_str1 = input("Enter elements of the first tuple separated by commas: ")
# tuple_1 = 
tuple_1 = (1, 2, 3, 4, 5)
# print(tuple_1)

# input_str2 = input("Enter elements of the first tuple separated by commas: ")
# tuple_2 = tuple(map(int, input_str2.split(',')))
tuple_2 = (4, 1, 7, 8, 2)
# print(tuple_2)

result = tuple(new_element for new_element in tuple_1 if new_element in tuple_2)

# print(result)




# 2. Create a Python program that generates a tuple of the first 20 Fibonacci numbers.

def fib():
    a, b = 0, 1
    c = 0
    ans = []
    ans.append(a)
    ans.append(b)
    while c < 20:
        c = a + b
        a = b
        b = c
        ans.append(c)
    return ans


fib_tuple = tuple(element for element in fib() )
# print(fib_tuple)/




# 3. Write a function in Python that takes a tuple of integers as input and returns the sum of all the even numbers in the tuple.

def fin_sum(ints):
    sum = 0
    for element in ints:
        if element%2 == 0:
            sum += element
    return sum


# input_tuple = input("Enter comma separted value for tuple input: ")
# mytuple = tuple(map(int, input_tuple.split(',')))
# print(mytuple)
# x = fin_sum(mytuple)
# print(x)

# 4. Implement a Python function that takes a tuple of strings as input and returns a new tuple with the strings sorted in alphabetical order.

string_tuple = ("banana", "apple", "orange", "kiwi", "grape")

result = tuple(sorted(string_tuple))
print(result)



# 5. Create a Python program that prompts the user to enter a series of numbers separated by commas, converts them into a tuple of integers, and then calculates and prints the sum of the squared values of the tuple elements.

# 6. Write a Python function that accepts a tuple of numbers and returns a new tuple with the elements in reversed order.

tuple_1 = (1, 2, 3, 4, 5)
# print(tuple_1)
# print(tuple_1[::-1])




# 7. Implement a Python program that takes two tuples of equal length containing numeric values and returns a new tuple where each element is the sum of the corresponding elements of the input tuples.

t_1 = (4, 6, 2, 8)
t_2 = (1, 3, 5, 7)

t_3 = tuple(t_1[i] + t_2[i] for i in range(len(t_1)))
print(t_3)

# 8. Write a Python function that takes a tuple of integers as input and returns a new tuple with only the unique elements from the input tuple.

question = (3, 5, 2, 7, 3, 2, 8, 5)

result = tuple(element for element in question if question.count(element) == 1)

# print(result)

# 9. Create a Python program that accepts a tuple of strings and prints the longest string from the tuple.

tuple_of_strings = ("apple", "banana", "kiwi", "strawberry", "orange")

# longest = ''
# for element in tuple_of_strings:
#     if len(element) > len(longest):
#         longest = element

# print(longest)

longest = max(tuple_of_strings, key=len)
print(longest)
    
