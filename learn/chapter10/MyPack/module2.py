class MyException(Exception):

    def __init__(self, password) -> None:
        super().__init__("Please enter with minimum 1 number character")


def number_checker(password):
    if not any(char.isdigit() for char in password):
        raise MyException(password)
    
    return "login success"
    




