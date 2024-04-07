'''
tuples are collection of different data type values 
cannot change after once created.
'''

a = (1,2, 3, 4, False, "Alok", (11, 20))
print(type(a))
print(a[0])
print(a[-1][0])

t1 = (1)
print(type(t1)) # convert into int not a tuple thus, provide a comma
t1 = (1,)
print(type(t1))
x = a.count(1)
print(x)

x, y, z, w, e, r, t = a
print(x, y, z)


