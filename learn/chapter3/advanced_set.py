# Given a list my_list = [1, 2, 3, 4, 5], how would you use slicing to extract the elements in reverse order?

y_list = [1, 2, 3, 4, 5]
print(y_list[::-1])


# Consider a 2D NumPy array arr of shape (3, 4). How would you select the last two rows of the array using slicing?

import numpy as np

array = np.array([[0, 1, 2, 4],
                  [3, 4, 5, 6],
                  [6, 7, 8, 9]])

last_row = len(array)
print(last_row - 2)
print(array[last_row - 2:])

# Suppose you have a string sentence = "The quick brown fox jumps over the lazy dog". How would you extract every third word from the sentence using slicing?

sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split(" ")
print(words)
result = "".join(words[::3])
print(result)


# Given a 3D NumPy array data of shape (5, 4, 3), how would you select all elements in the first and last dimensions, but only the first two elements along the second dimension?

import numpy as np

# Create a 3D NumPy array of shape (5, 4, 3)
data = np.random.randint(0, 10, size=(5, 4, 3))

print(data)
selected_elements = data[:, :2, :]
print("Answer", selected_elements)

# Imagine you have a list my_list = [10, 20, 30, 40, 50, 60]. How would you use slicing to select every alternate element starting from the second element?

my_list = [10, 20, 30, 40, 50, 60]
print(my_list[1::2])

# Suppose you have a 2D NumPy array matrix of shape (5, 5) filled with integers. How would you extract the diagonal elements of the matrix using advanced slicing?
print("--------------5-----------------------")
array_random = np.random.randint(0, 10, size=(5, 5))
# print(array_random)

# diagonal_elements = array_random[range(5), range(5)]
# print(diagonal_elements)
# # print(array_random[::,4])

row_count = 0
col_count = 0
while (row_count < 5 and col_count < 5 ):
    # print(array_random[row_count, col_count])
    row_count += 1
    col_count += 1

row_count = 4
col_count = 4
while (row_count > 0 and col_count > 0):
    # print(array_random[row_count, col_count]);
    row_count -= 1
    col_count -= 1

# Consider a list my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]. How would you use slicing to reverse the order of elements in groups of three?

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)
# Reverse the order of elements in groups of three using slicing
reversed_groups_of_three = my_list[::-1]
grouped_reversed_list = [reversed_groups_of_three[i:i+3] for i in range(0, len(reversed_groups_of_three), 3)]

print(grouped_reversed_list)



# Given a string word = "python", how would you create a new string by alternating the cases of its letters (i.e., 'pYtHoN') using slicing?

word = "python"

# Create a new string by alternating the cases of its letters using slicing

count = 1
new_word = ''
for ch in word:
    if count == 2:
        new_word += ch.upper()
        count = 1
    else:
        new_word += ch.lower()
        count += 1


# using slicing

every_second_char = word[1::2].upper()
normal_chars = word[::2]
print(normal_chars)
print(every_second_char)
print(result)
print(new_word)