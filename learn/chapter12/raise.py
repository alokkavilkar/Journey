def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Enter number please")
        
try:
    print(increment('a'))
except Exception as e:
    print(e)


# custom exception with class

class MyException(Exception):
    def __init__(self, password):
        self.number = password
        super().__init__('Enter character with less then 10 length')
    
    
class SymbolException(Exception):
    
    def __init__(self, password):
        self.password = password
        super().__init__('Enter a symbol $ in password please..')
        
def login(password):
    if len(password) > 10:
        raise MyException(password)
    if password.count('$') == 0:
        raise SymbolException(password)
    return "Login success...."

try:
    result = login('alokkav$')
except MyException as e:
    print(e)
except SymbolException as s:
    print(s)
else:
    print(result)
