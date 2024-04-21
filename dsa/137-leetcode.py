# 137. Single Number II
nums = [2,2,2,1]  #Output: 3

# Brute force
map = {}

for element in nums:
    if map.get(element) != None:
        map[element] += 1
    else:
        map[element] = 1

for key, _ in map.items():
    if _ == 1:
        print(f'Naive brute force solution : {key}')
        break


# bit manipulation

ans = 0
for i in range(0, 32):
    cnt = 0
    for element in nums:
        val = element & (1 << i)
        if val != 0:
            cnt+=1
    
    if cnt % 3 == 1:
        ans  = ans | (1 << i)

# we need to modify for large test case with negative numbers
print(ans)

# 3rd best approach

ones=0
twos = 0

for i in nums:
    ones = (ones ^ i) & ~twos
    print(ones)
    twos = (twos ^ i) & ~ones
    print(twos)

print(ones)



