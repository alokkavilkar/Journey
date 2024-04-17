from typing import Union
class Car:

    def __init__(self, make:str, model:str, year:Union[str, int]) -> None:
        self.make = make
        self.model = model
        self.year = year

    def display_info(self) -> str:
        if isinstance(self.year, str):
            return "Invalid Year"
        else:
            return f"{self.make}'s this {self.model} has released in {self.year}"

hyundai = Car('hyundai', 'c89', 2003)
print(hyundai.display_info())

# print(isinstance('2003', str))
# print(isinstance(hyundai, Car))


class Employee:

    salary = 0
    name = ''

    def __init__(self, name:str, salary:str) -> None:
        self.name = name
        self.salary = salary

    def print_info(self) -> str:
        if isinstance(self.salary, str):
            return f"{self.salary} is not valid (data type)"
        
        else:
            return f"{self.name}'s salary is {self.salary} working in {self.company}"
        
    @staticmethod
    def greet():
        print("Good morning, sir")
        # print(self.company)
        # print(salary)
        print(Employee.salary)
        
alok = Employee('Alok', 25)
alok.company = 'google'
print(alok.print_info())
# alok.print_info() converts into Employee.print_info(alok) as object reference on top of which self points towards the object passed thus self keywords refers to object instance variables and class variables as well

# static methods
alok.greet()
# without pointing to object referes to only class
Employee.greet()




