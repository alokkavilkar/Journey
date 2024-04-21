# # Question 1: Nested Dictionary Operations
#  Define a function merge_dicts(d1, d2) that merges two dictionaries d1 and d2. If a key is common to both dictionaries, the value in d2 should overwrite the value in d1. Additionally, if a value in either dictionary is itself a dictionary, recursively merge those dictionaries.


def merge_dicts(d1, d2):
    ans_dict = {}
    for x, y in d1.items():
        if d2.get(x) != None:
            if type(d1.get(x)) == dict:
                temp = {}
                for a, b in d1.get(x).items():
                    temp[a] = b
                
                # temp[x] = d2.get(x)
                for a, b in d2.get(x).items():
                    temp[a] =b
                print(temp)
                ans_dict[x] = temp

            else:
                ans_dict[x] = d2.get(x)
        else:
            ans_dict[x] = y


    return ans_dict

d1 = {'a': 1, 'b': {'x': 2, 'y': 3}}
d2 = {'b': {'z': 4}, 'c': 5}


result = merge_dicts(d1, d2)
# print(result)
# Output: {'a': 1, 'b': {'x': 2, 'y': 3, 'z': 4}, 'c': 5}

# Define a function common_keys(d1, d2) that returns a set of keys common to both dictionaries d1 and d2.

def common_keys(d1, d3):
    ans_set = set()
    copy = d1.copy()

    for x,_ in d2.items():
        if d1.get(x) != None:
            ans_set.add(x)

    return ans_set

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 4, 'c': 5, 'd': 6}
result = common_keys(d1, d2)
print(result)
# Output: {'b', 'c'}

# Define a function flatten_dict(d) that flattens a nested dictionary d into a single-level dictionary where keys are composed of nested keys joined by underscores.

def flatten_dict(d):
    result = {}

    for x, _a in d.items():
        if type(d.get(x)) == dict:
            for a, _ in d.items():
                if type(d.get(a)) == dict:
                    for q, w in d.get(a).items():
                        new_x = x+'_'+a+'_'+q
                        result[new_x] = w
                else:
                    new_x = x + "_" + a
                    result[new_x] = _
        else:
            result[x] = _a
    
    return result





d = {'a': 1, 'b': {'x': 2, 'y': {'z': 3}}}
result = flatten_dict(d)
print(result)
# Output: {'a': 1, 'b_x': 2, 'b_y_z': 3}

# Define a function invert_dict(d) that inverts a dictionary d, where keys become values and values become keys. If multiple keys have the same value, the inverted dictionary should have a list of corresponding keys.
def invert_dict(d):
    map_count = {}
    for x, y in d.items():
        if map_count.get(y) !=  None:
            list_1 = [element for element in map_count.get(y)]
            list_1.append(x)
            map_count[y] = list_1
        else:
            map_count[y] = x
        
    return map_count

d = {'a': 1, 'b': 2, 'c': 1}
result = invert_dict(d)
print(result)
# Output: {1: ['a', 'c'], 2: 'b'}



