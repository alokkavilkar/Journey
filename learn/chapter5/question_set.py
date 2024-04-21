
# 1. **Question 1**: Given two sets `set1` and `set2`, write a function to return the intersection of the two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

new_set = set1.intersection(set2)
print(new_set)


# 2. **Question 2**: Explain the difference between the `add()` and `update()` methods in sets with examples.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.add(6)
print(set1)
set1.update({7, 8})
print(set1)

# 3. **Question 3**: Write a Python function to remove all duplicates from a given list and return the unique elements as a set.

list = [1, 3, 3, 2, 2, 4, 6, 4, 1]
new_set = set(element for element in list)
print(type(new_set))


# 6. **Question 6**: Explain the concept of symmetric difference between sets and provide an example.

# Example
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

diff = A.symmetric_difference(B)
print(diff)

# Updates in place with update symetric function
A.symmetric_difference_update(B)
print(A)


# 7. **Question 7**: Write a Python program to create a set containing the unique characters present in a given string.

str = "alaokk"
str_set = set(element for element in str)
print(sorted(str_set))


# Advanced

# Q.1  Write a function to find the Cartesian product of two sets.

def cartesian_product(a, b):
    ans_set = set()
    for element in a:
        for x in b:
            ans_set.add((element, x))

    return ans_set

set1 = {1, 2}
set2 = {'a', 'b', 'c'}
result = cartesian_product(set1, set2)
print(result)  # Output: {(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')}


#  Implement a function to find the power set of a given set.

def power_set(input_set):
    ans_set = {()}  # Initialize with an empty set
    for element in input_set:
        new_subsets = set()  # Temporary set to store new subsets
        for subset in ans_set:
            print(element)
            print(subset)
            new_subsets.add(subset + (element, ))
            print(subset + (element,))
            print(ans_set)
            print(new_subsets)
        
        ans_set.update(new_subsets)
    return ans_set


input_set = {1, 2, 3}
result = power_set(input_set)
print(result)  # Output: {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}

# t1 = (1,2)
# t2 = (3, 4)
# print(t1 + t2)

# Write a function to determine if a given set is a subset of the power set of another set.

def is_subset_of_power_set(x, y):
    ans_set1 = power_set(x)

    return y.issubset(ans_set1)


set1 = {1, 2}
set2 = {(), (1,), (2,), (1, 2)}
result = is_subset_of_power_set(set1, set2)
print(result)  # Output: True

# Intersection of multiple sets

def intersection_of_sets(set):
    map_count = {}
    for subset in sets:
        for element in subset:
            if map_count.get(element) != None:
                map_count[element] = map_count.get(element) + 1
            else:
                map_count[element] = 1

    max = 0
    ans = 0
    for x, y in map_count.items():
        if y > max:
            ans = x
            max = y
    return ans

def intersection_of_sets2(sets):
    if not sets:
        return set()
    
    # Initialize intersection with the first set
    result = sets[0]
    
    # Compute intersection with each subsequent set
    for subset in sets[1:]:
        result = result.intersection(subset)
    
    return result



sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
result = intersection_of_sets(sets)
print(result)  # Output: {3}


# Implement a function to efficiently find the symmetric difference of multiple sets.

def symmetric_difference_of_sets(set):
    if not set:
        return set()
    
    sample = set[0]

    for subset in set[1:]:
        sample = sample.symmetric_difference(subset)
        # print(result)

    return sample

sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
result = symmetric_difference_of_sets(sets)
print(result)  # Output: {1, 5}


# Write a function to find the largest subset of a given set such that no two elements are divisible by each other.


