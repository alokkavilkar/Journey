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

def function(name, lists):
    for list_ in lists:
        print(list_)
    print(name)

list1 = [[1, 2, 3], [2, 3, 4]]
# function("alok", list1)


# if mentioned parameter is default then can be argued with non sequence based argument.
def defaultArg(name="stranger", another=0):
    print(name, another)
    
defaultArg(another=10, name="alok")

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)
    
print(factorial(5))


# args and kwargs:

# Positional arguments are collected into a tuple, allowing the function to handle any number of them.
# Keyword arguments are collected into a dictionary, allowing for flexible and descriptive argument passing.
# Mixing Arguments: When using both, positional arguments must come before keyword arguments when calling the function.

# takes only vlaue args and convert it into tuples
def func1(*args):
    for v in args:
        print(v, end=" ")
        
# takes variables and value as much as possible

def func2(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
        
func1(1, 2, 3, 4, 5, 6, 7, 8)
func2(a=10, b=20, c=30)



# Decorators takes fucntions and can access varibales and can call another function and return its wrapper

print("------------------------------------------------------------")
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper
    
def value(func):
    def wrapper(args):
        print("arguments are", args)
        return func(args)
    return wrapper
    
    
@value
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")



