import os

folder = 'C:\\Users\\Laptop\Desktop\\'
file_to_create = 'newfile.txt'
custom_folder = 'New Folder'
path = os.path.join(folder, custom_folder, file_to_create)
print(path)

if os.path.isdir(path):
    print("Folder already created with file init.")

else:
    # os.makedirs(os.path.join(folder, custom_folder))

    # with open(path, 'w') as f:
    #     f.write("Hello in file")
    #     f.close()
    pass

print("Done")

with open('access.log', 'r+') as f:

    for line in f:
        print(line)

    
with open('access.log', 'a+') as f:

    f.write("New input")

    for line in f:
        print(line)

    




