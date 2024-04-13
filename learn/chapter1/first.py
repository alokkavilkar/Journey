import os

# print(os.cpu_count());
# print(os._exit(0));

print ('''Hello World''')

# This is comment

'''
    This is multiline comment
    You can write here as well
'''

# print ("THis is printint
#        "). Generates errors

print ('''THis is new line
          this is new line
       ''')

a = '''New variable'''

print(type(a))
# print(os.get_terminal_size())
base_dir = 'C:\\Users\\Laptop\\Desktop\\main-server\\Python'
project = "python_project"
os.path.join(base_dir, project)


# Base directory
base_dir = 'C:\\Users\\Laptop'

# Subdirectories
sub_dir1 = 'Desktop'
sub_dir2 = 'main-server'
sub_dir3 = 'Python'

# File name
file_name = 'learn'

# Construct the file path using os.path.join()
file_path = os.path.join(base_dir, sub_dir1, sub_dir2, sub_dir3, file_name)

print(file_path)
print(os.path.dirname(file_path))
os.makedirs(os.path.dirname(file_path), exist_ok=True)
print(os.path.exists(file_path))
cpus = os.cpu_count
if cpus in range(0, 3):
    print('Wow, yours processing time increased')
else :
    print('Whats to say now you don;t have much resources')


