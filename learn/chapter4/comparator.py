
from functools import cmp_to_key

def my_comparator(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

# Example usage
data = [3, 1, 4, 1, 5, 9, 2]
sorted_data = sorted(data, key=cmp_to_key(my_comparator))
print(sorted_data)  # [1, 1, 2, 3, 4, 5, 9]
