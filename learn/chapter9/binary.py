# a = int(input('Enter number whose binary you want: '))
a = 7
# binary format = 111
binary_no = 0

for i in range(0, 33):
    val = a & 1
    binary_no += pow(10, i) * val
    a = a >> 1

print(binary_no)


# one's complement

''' 7-> 111 one's complement is 000 and 2's complement is 000 + 1 = 001'''

a = 7
# 7 => 0111 => 1000 
print(~a)
one_complement = ~a
twos_complement = one_complement + 1
print(twos_complement)
binary_no = bin(twos_complement)
print(binary_no)






