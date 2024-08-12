from functools import cmp_to_key

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
