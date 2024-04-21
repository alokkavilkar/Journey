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


