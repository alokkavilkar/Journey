print("Numbers------------------")

var = 2 + 3
var = 3 * 2
var = 3 // 2 # returns the floor of the division value.
var = 3 / 2  # returns the float value in python3 whereas returns floor value in python2
print (var)


print("Floats --------------------------")

var = 0.1 + 0.1
var = 2 + .1
var = 0.2 + 0.1
print(var)

# Complex

z = 2 + 1j
z1 = 3 + 2j
print(z + z1)

'''**Binary Types:**
   - **bytes**: Represents immutable sequences of bytes. Example: `data = b'Hello'`
   - **bytearray**: Represents mutable sequences of bytes. Example: `data = bytearray(b'Hello')`'''

data = b'Alok'
print(data)
# for bytes in data:
#     print(bytes)


data = b'01'
# for val in data:
    # print(val)

data = 4
number = 0
while (data != 0):
    new_val = data & 1
    # print(new_val)
    data = data >> 1

data = 101
decimal = 0
count = 0
while(data != 0):
    new_val = data%10  # Extract the last digit
    print(new_val)
    if new_val == 1:
        decimal += 2 ** count
    count += 1
    data = data // 10  # Remove the last digit

print(decimal)

data = 'Alok'
list = []
# for val in data:
    # new_val = ord(val) - ord('A')
    # print(new_val)

data = bytearray(b'alok')
for val in data:
    print(val)


print(round(7.8379,  2))
print(round(7.8379, 1))
print(round(7.8379, 0))

print(round(784, -1)) # => takes from 4 to calculate next 78 so 780
print(round(784, -2))
print(round(784, -3))


# print(10.0 /  3)
# print(10.0 // 3)

# print(10 / 3)