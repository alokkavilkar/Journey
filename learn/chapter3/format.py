# For example, if you call printsalary(50000), it will print 50,000.00 to the console.

'''
d: Format as an integer.
f: Format as a floating-point number.
s: Format as a string.
%: Format as a percentage

,: Use commas as thousand separators.
_: Use underscores as separators.
.: Use periods as separators.

'''

# Format an integer with commas as thousand separators
formatted_int = '{:,d}'.format(1000000)
print(formatted_int)  # Output: 1,000,000

# Format a floating-point number with 3 decimal places and commas as thousand separators
formatted_float = '{:,.3f}'.format(1234567.8901234)
print(formatted_float)  # Output: 1,234,567.890

# Format a string with underscores as separators
formatted_string = '{:_s}'.format('HelloWorld')
print(formatted_string)  # Output: Hello_World

# Format a percentage with 2 decimal places
formatted_percentage = '{:.2%}'.format(0.75)
print(formatted_percentage)  # Output: 75.00%


str = 'alokkavilkar'
print(str.capitalize())
print(str.count('a'))

print("{:d}".format(1000))
print("{:,d}".format(1000))
print("{:,f}".format(10000))
print("{:,.2f}".format(1000))
print("{:,.5f}".format(1000))


# 10 * 100 => return float string
print("{:%}".format(10))
#  0.75 * 100 => 
print("{:.2%}".format(0.75))

# String format

print("{:,}".format(1000))

print("{:>10}".format("hello"))
print("{:>10d}".format(1234))
print("{:^10}".format(1234))


print('{:^20}'.format(str))

# is same as 

print(f'{str:^20}')
