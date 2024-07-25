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


val = sorted(dic.keys(), key=cmp_to_key(comparator))
dict1 = {v: dic[v] for v in val}
print(dict1)

dict1 = dict(sorted(dic.items(), key=cmp_to_key(comparator)))

             
