
# 1. **Question:** Given two tuples `tuple1 = (1, 2, 3)` and `tuple2 = (4, 5, 6)`, write a comprehension to generate a new tuple containing the product of corresponding elements of the input tuples.

tuple1 = (1, 2, 3) 
tuple2 = (4, 5, 6)

result = tuple(tuple1[i] * tuple2[i] for i in range(len(tuple1)))
print(result)


# 2. **Question:** Suppose you have a tuple `numbers = (1, 2, 3, 4, 5)`, write a comprehension to create a new tuple containing only the even numbers from the input tuple.

numbers = (1, 2, 3, 4, 5)

result = tuple(element for element in numbers if element%2 == 0)
print(result)

# 3. **Question:** Consider two tuples `tuple1 = ('a', 'b', 'c')` and `tuple2 = ('x', 'y', 'z')`, write a comprehension to generate a new tuple where each element is a concatenation of one element from `tuple1` and one element from `tuple2`, in the form of `(a, x), (b, y), (c, z)`.

tuple1 = ('a', 'b', 'c')
tuple2 = ('x', 'y', 'z')

result = tuple((a, b) for a, b in zip(tuple1, tuple2))
print(result)

# 4. **Question:** Given a tuple of strings `words = ('apple', 'banana', 'cherry', 'date')`, write a comprehension to create a new tuple where each element is the length of the corresponding string in the input tuple.

words = ('apple', 'banana', 'cherry', 'date')

ans = tuple(len(word) for word in words)
print(ans)

# 5. **Question:** Suppose you have two tuples `t1 = (1, 2, 3)` and `t2 = (4, 5, 6)`, write a comprehension to generate a new tuple where each element is a tuple containing the sum and the difference of the corresponding elements from `t1` and `t2`.

t1 = (1, 2, 3)
t2 = (4, 5, 6)

result = tuple((a + b, b - a) for a ,b in zip(t1, t2))
print(result)