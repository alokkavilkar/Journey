# Write a Python function to set the nth bit of a given integer to 1.

num = 11
k = 3

print(num ^ (1<<(k-1)))

print((1<<(k-1)) & 0)