class MyException(Exception):
    def __init__(self, password) -> None:
        self.password = password
        super().__init__('Password length must be less than l0')


def password_length(passwd):
    if len(passwd) > 10:
        raise MyException(passwd)
    return "Login success"