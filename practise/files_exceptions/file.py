with open('file.txt', 'r') as f:
    content = f.read()

# with open('file.txt', 'r') as f:
#     line = f.readline()

#     while line :
#         print(line.strip())
#         line = f.readline()

with open('file.txt', 'r+') as f:

    lines = f.readlines()
    
    for i, line in enumerate(lines):
        # print(line)
        if line.lower().startswith('server'):
            # print('Yes')
            # print(len(lines))
            if i + 1 < len(lines) and not lines[i+1].lower().startswith('status'):
                lines.insert(i+1, 'status:online\n')

    f.seek(0)
    f.writelines(lines)


try:
    with open('file.txt', 'r') as f:
        lines = f.readlines()
except FileNotFoundError as e:
    print(f'Ensure file is there , {e}')
else:
    print("This will print if try do its job well.")


import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)






# print(content.rstrip())