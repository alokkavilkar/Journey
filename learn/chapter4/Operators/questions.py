#  Q.1  Given two numbers a and b, write a Python function to compute the result of (a * b) + (a / b) - (a % b).

a = 10
b = 3

def compute(a, b):
    # a * b = 10 * 3 = 30 a / b = 10 / 3 = 3.333 a %b = 10 $ 3 = 1 30+ 3.333 + 1
    return (a * b) + (a / b) - (a % b)

print(compute(a, b))

#  Q.2 Write a Python program to swap the values of two variables x and y without using a temporary variable.

def swap (x, y):
    temp = y
    y = x
    x = temp
    return x, y

def without_temp(x, y):
    # x madhe doni tak x madhna y kadh manje tula fakt x takta yel y madhe 
    x = x + y # 10 + 5 = 15
    y = x - y # 15 - 5 = 10
    x = x - y # 15 - 10 = 5
    return x, y 

x = 10
y = 5
print(x, y)
# x, y = swap(x, y)
x, y = without_temp(x, y)
print(x, y)


#  Q.3 Write a Python function to determine whether a given year is a leap year or not.

year = 2021
if year %4 == 0 : print("Leap year : true") 
else: print("Not a leap year")

# Q.4 Write a Python function to determine if a given number num is divisible by both 2 and 3.

def division(a):
    return a % 2 ==0 and b % 3 == 0
a = 12
print(division(a))
b = 10
print(division(b))

#  Q.5  Write a Python function to count the number of occurrences of a given element x in a list lst

lst = [1, 2, 3, 4, 2, 2, 5]
x = 2
# Expected output: 3

def count(list, a):
    cnt = 0
    for x in list:
        if a is x:
            cnt += 1

    return cnt

# print(count(lst, x))

# Q.6 Write a Python function to toggle the nth bit of a given integer num.

num = 10  # Binary representation: 1010
n = 2
# After toggling the 2nd bit, num should be 14 (1110 in binary)


#  3 => 4 - n + 1
bin = 0
i = 0
while num != 0:
    val = num & 1
    # print(val)
    if i == (4 - n):
        # print(val, i, (4 - n + 1))
        val = val | 1
        # print (val)
    bin =  pow(10, i) * val + bin
    i += 1
    num = num >> 1

print(bin)

# int setBit(int n, int k) 
# { 
#     return (n | (1 << (k - 1))); 
# } 
  
# // Function to clear the kth bit of n 
# int clearBit(int n, int k) 
# { 
#     return (n & (~(1 << (k - 1)))); 
# } 
  
# // Function to toggle the kth bit of n 
# int toggleBit(int n, int k) 
# { 
#     return (n ^ (1 << (k - 1))); 
# } 
n = 10
k = 2

print(n ^ (1<<(k-1)))








