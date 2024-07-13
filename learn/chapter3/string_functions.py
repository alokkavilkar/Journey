str = 'alok'

print(str)
print(type(str))

# for char in str:
#     print(char)

print(str.find('a'))
print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.casefold())



print(str.count('a'))
print(str.encode())
# str = str.expandtabs(10)
print(str.isalpha())
print(str.isnumeric())
print(str.title())

str = '    alok     '
print(str + "l")
print(str.ljust(20))       # add the non-strip to string
print(str.rstrip() + "l")  # cuts the strip to string
print(str.lstrip() + 'l')
print(str.strip() + ' l')

str2 = 'alok'
print(str2.ljust(20), '9')

str = '         alok, maury, michal, jackson           '
print(str.strip().split(','))

str = '1-2-3-4'
print(tuple(map(int,str.split('-'))))

str = 'alok \n kavilkar'
print(str.splitlines())

print(str.rpartition('\n'))

# a = input("Enter the numbers")
# print(list(map(int,a.split(','))))




str = 'alok'
newstr = 'New'.join(str)
newstr = 'new'.join(['alok'])   # since no way to append with list of element returns single element
newstr = ','.join(['alok', 'ram', 'mumbai'])
print(newstr)
print(newstr.split(','))
    
    
