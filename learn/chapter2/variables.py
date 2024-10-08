# ----------------------- Binary format ----------------------------------------------

String.valueOf(10) = "10"
str(10)                     = "10"
Integer.parseInt("10") = 10
int("10")                 = 10
Integer.parseInt("1101", 2) = 1101 in bytes
int("1101")  = 1101
Integer.toBinaryString(10) = "1010"
bin(10)                         = "0b1010"

# binary data 
binarydata = 0b1101
# always convert automatically to equivalent number.
'''
    str = binarydata[2:]
    return int(str, 2)
'''
print(binarydata)

# number to string 
var1 = 10
print(str(var1))

# string to number
var2 = "10"
print(int(var2))

# string number to binary number
binary = "1101"
print(int(binary), int(binary, 2))

# number to binary format (string)
print(bin(13))

# ----------------------------------------------------------------------------------

x = 10
y = 'Hello'
z = 20.05

a, b, c = 5, 6.6, 'New Hello'

# variable reassignment
x = 20
x = "Newest Hello"

def function_for_local_variable():
    new_variable = 20
    print("Function's variable can't be used outside of function : ", new_variable)


function_for_local_variable()
# print(new_variable)

_str = "Alok"
# _str = _str.join("New")
# print(_str)

_str = "".join(["New ", _str])
print(_str)

_number = "20"
print(int(_number))
_number = int(_number)
_str_number = 20
print(type(_number), _number)
print("Type of number _str_number is ", type(_str_number))
_str_number = str(_str_number)
print(type(_str_number), _str_number)

str_2 = "ada shelby"
print(str_2.title())
print()

question = "   String with spaces   "
list = [question.strip().split(" ")]


