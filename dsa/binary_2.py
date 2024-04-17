# Q.1 swap two numbers;

a = 10
b = 20

temp = a
a = b
b = temp
print(a, b)

''' with bit manipulation '''
a, b = 10, 20
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

# Q.2 is ith the set bit

n = 13
i = 1
#  1101 ith bit is set  1101 & 100 => 1

print((n & (1 << i)) > 0)

# Q.3 set ith bit 

# 1101 i = 1 => 1111

n = 13
i = 1
print(n | (1 << i))


# Q.4 clear ith bit

n = 5
i = 2
# 101 => 001

print(n & ~(1<<i))

# Q.5 toggle the bits

n = 13
i =2 

# 1101 => 1001

print(n ^ (1 << i))



