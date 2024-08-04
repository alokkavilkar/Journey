import MyPack

password = 'alok2'

try:
    length = MyPack.password_length(password)
    has_number = MyPack.number_checker(password)
except Exception as e:
    print(e)
else:
    print(f"Password length: {length}, Contains number: {has_number}")