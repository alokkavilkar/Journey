# functions are nothing but group of code that executes on invoking.

def percent(list1):
    return list1[0]

list = [1, 2, 3, 4, 5]
x = percent(list)
print(x)


# 0 1 1 2 3 5 8 13 21 34 55

def fib(n):
    list = []
    a = 0
    b = 1
    list.extend([a, b])
    c = 0
    while c < n:
        c = a + b
        a = b
        b = c
        list.append(c) 
    
    return list

ans = fib(10)
print(ans)

# multiple argument values;

def argumental_function (*arg, default='no'):
    for i in arg:
        print(i, end=' ')

    print(default)

argumental_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, default='This has passed by function invoker.')

# Recursion

# n! = n * (n - 1) * (n - 2) ...... 1

def factorial(n):

    if n == 1:
        return n
    
    return n * factorial(n - 1)


f = factorial(5)
print(f)

