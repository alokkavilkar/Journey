# File to demonstate string python

name = 'alok'
for ch in name:
    # val = (int)(ord(ch))
    # print(val)
    # print(ord(ch), "->", ch)
    pass

# print('a' + 'l')

# slicing the python string based on inbuilt function defined.

name = 'alok'
print(name[0])
# name[3] = 'N'
print(name[0:3])
print(name[-4])

print(len(name))

# to change string character only way. 
new_name = name[0:3] + 'N' + name[4:]
print(new_name)
print(new_name[:4])
print(new_name[0:])
new_name = 'aloka'
print(new_name[::2])
print(new_name[1::3])
print(new_name[-5:-1]) # -5 included which is a and -1 < so its -2 'k'

'''
Index hote he 0 se start
Index hote he negation of 1 se start
[0:4] 0 start included and 4 tak but < 4
[::]  starting se end tak
[::2] starting se end tak lekin 2 ko chodke. like aloka -> aoa
'''

name = 'alok'
print('Left with 2 steps', name[::2]) # its ao
# reverse
print(name[::-1])
print(name[-3:])
print(name[:])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][1])  # Access the element at row 0, column 1
matrix[0][1] = -1
print(matrix[0][1])
print(matrix)

import numpy as np

array = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8],
                  [6, 7, 6]])

# print(array[::2]) same as arra[..., 2]
print(array[1:3])
print(array[1,2:])
print(array[::,2:])





