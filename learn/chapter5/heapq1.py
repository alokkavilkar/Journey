from functools import cmp_to_key
import heapq

def comparator(a, b):
    if a < b: return -1
    elif a > b : return 1
    else: return 0
    
    
dic = {
    'e': 10,
    'c': 2,
    'd':1,
    'a':4,
    'b':3,
}

def comparatornew(item1, item2):
    # print(item1)
    if item1[1] < item2[1]: return -1
    elif item1[1] > item2[1] : return 1
    else: return 0
    
# val = sorted(dic.keys(), key=cmp_to_key(comparator))
# print({v : dic[v] for v in val})

val = dict(sorted(dic.items(), key=cmp_to_key(comparatornew)))
print(val)

def heapcompare(item):
    return item[0]
    
    
li = [("alice", 5), ("mahesh", 10), ("alok", 12), ("alices", 2), ("alo", 1)]

heapq.heapify(li)
print(heapq.nlargest(4, li, key=heapcompare))

def compareto(item):
    return item[1]

print(sorted(li, key=compareto))

