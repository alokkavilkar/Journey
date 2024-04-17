# decimals to binary
n = 13 # 1101

bin = 0     
index = 0                              
while n!= 0:
    val = n & 1
    bin += pow(10, index) * val
    index+=1
    n = n >> 1

print(f'decimal values  binary number is {bin}')


# binary to decimal
bin = 1101
n = 0
i = 0
while bin != 0:
    val = bin % 10
    if val == 1:
        n += pow(2, i)
    i += 1
    bin = bin // 10

print(n)

# 1's complement = 1101 => 0010
n = 13
print(~(n))

# 2s compliment = 1101 => 0010 + 1 => 0011
n = 5
n = ~(n)
n = n + 1
print(n)

# because 2s' complement of a number is negative of itself.





