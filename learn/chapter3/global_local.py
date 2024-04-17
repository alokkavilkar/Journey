# Global and Local variables

# defined global scopedby natural
x = 10

def my_functions():
    # local scoped.
    y = 20
    print(x) # can access the global variables.
    print(y)

my_functions()
# print(x, y) y is not defined

def my_function2():
    global x #take the global veriable and modify it.
    x = 20
    print(x)

print(x)
my_function2()
print(x)

# for i in range(20):
#     print(i)

# print(i)

def modifier():
    global i
    i = 20
    print(i)

modifier()
print(i)
