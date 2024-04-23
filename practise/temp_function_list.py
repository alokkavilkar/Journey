

def printing_of_language(list_1):
    while list_1:
        val = list_1.pop()
        print(val)

    print(list_1)

list_1 = ['python', 'java', 'golang', 'manuscript']

# passing the list_1's copy to function.
printing_of_language(list_1[:])
print(list_1)

first, *_, last = [1, 2, 3, 4, 5]
print(_)



