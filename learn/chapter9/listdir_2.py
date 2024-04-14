import os


def list_file_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "You don;t have much permission"
    



folder = input("Enter folder to get list of files init").split()

files, error_message = list_file_in_folder(folder[0])

print(folder)
if len(files) == 0:
    print('Sorry don;t have much files to show')

if files:
    for file in files:
        print(file)

