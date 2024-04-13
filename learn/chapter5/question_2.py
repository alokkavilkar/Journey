# Write a Python function to remove duplicate elements from a given list and return a set of unique elements.

def remove_duplicates(list):
    return set(element for element in list)

input_list = [1, 2, 3, 4, 2, 3, 5]
result = remove_duplicates(input_list)
print(result)  # Output: {1, 2, 3, 4, 5}


# Implement a function to check if two sets are disjoint (i.e., they have no common elements).

def are_disjoint(set1, set2):
    return all(element not in set2 for element in set1)


set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = are_disjoint(set1, set2)
print(result)  # Output: True


#  Write a Python program to find the union of multiple sets without duplicates.

def union_of_sets(sets):
    ans_set = set()
    for subset in sets:
        ans_set.update(subset)

    return ans_set

sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
result = union_of_sets(sets)
print(result)  # Output: {1, 2, 3, 4, 5}



# Question 4: Implement a function to compute the difference between two sets and return the result as a set.

def set_difference(set1, set2):
    return set(set1.difference(set2))

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
result = set_difference(set1, set2)
print(result)  # Output: {1, 2}




