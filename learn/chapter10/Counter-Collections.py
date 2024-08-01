# A Python program to show different 
# ways to create Counter 
from collections import Counter 
  
# With sequence of items  
list1 = [1, 2, 3, 4, 2, 1, 1, 1, 1, 2]
a = Counter(list1)

# from list of list
items1 = [[1,1],[4,5],[3,8]]
items2 =  [[3,1],[1,5]]
b = Counter(dict(items1)) + Counter(dict(items2))
print(b)

# from tuple of tuple
items1 = ((1, 2), (10, 3), (4, 5))
c = Counter(dict(items1))
print(c)

# from dict
Dict = {6:7, 8:9, 10:10}
d = Counter(Dict)
print(d)

# from keywords;
print(Counter(A=3, B=4, C=6))

