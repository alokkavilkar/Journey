print("Numbers------------------")

var = 2 + 3
var = 3 * 2
var = 3 // 2 # returns the floor of the division value.
var = 3 / 2  # returns the float value in python3 whereas returns floor value in python2
print (var)

# Python 2
>>> 10.0 / 3
3.3333333333333335
>>> 10.0 // 3
3.0

# Python3
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3

print("Floats --------------------------")

var = 0.1 + 0.1
var = 2 + .1
var = 0.2 + 0.1
print(var)

# Complex
print("-------------Complex---------------")
z = 2 + 1j
z1 = 3 + 2j
print(z + z1)

'''**Binary Types:**
   - **bytes**: Represents immutable sequences of bytes. Example: `data = b'Hello'`
   - **bytearray**: Represents mutable sequences of bytes. Example: `data = bytearray(b'Hello')`'''

print("--------------------- Bytes ---------------------")
# bytes => immutable sequence of bytes for binary data 0-255 each.
b = b'hello'
print(b)
# b[0] = 'Z' error as they are immutable
# ASCII value of H
print(b[0])

data = b'Alok'
print(data)
# always give you the ASCII Value.
# for bytes in data:
#     print(bytes)

data = b'01'
# for val in data:
    # print(val)

print("---------------------------- Bytearray ----------------------------")
# bytearray => mutable sequence upto 0 - 0-255
ba = bytearray(b'01')
print(ba) # = 48 49
# change to 50 ~= 2
ba[0] = 50
print(ba)  # 50 49

print("--------------------------- Memory View ---------------------------------")
# memoryview
# same as bytes but It is useful for efficiently handling large datasets or parts of binary data.
b = b'Hello'
mv = memoryview(b)
print(mv[0], b[0], ord('H'))
# what is byte => smallest form and character has smallest form as ASCII thus all return same.

# -------------------------------------------------------------------------

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




print(round(7.8379,  2))
print(round(7.8379, 1))
print(round(7.8379, 0))

print(round(784, -1)) # => takes from 4 to calculate next 78 so 780
print(round(784, -2))
print(round(784, -3))


# print(10.0 /  3)
# print(10.0 // 3)

# print(10 / 3)


'''
   Ord => returns unicode value for single character if two character given then raises typerror, if no character given then too.
   chr => takes unicode value and returns character for that value = char(3) => smiley and char(3 + ord('a') => c
'''

print(ord('a'))
print(ord('0'))
print(ord('😊')) 

print(chr(ord('a')))

# if no character provided then valueError
# if 'ab' is given then TypeError as single is required 'a'

print(chr((ord('b') - ord('a')) + 3 + ord('a')))


print(chr(1 + ord('a')))
# b =-> c
print(chr((ord('b') - ord('a') + 1) % 26 + ord('a')))
print(chr(2 + ord('a')))


# design a caesor chiper with text and shift

def caesor_chiper(text, shift):
    output = ''
    for char in text:
        new_chr = chr((ord(char) - ord('a') + shift)%26 + ord('a'))
        output += new_chr

    print(output)

caesor_chiper('abcd', 1)
