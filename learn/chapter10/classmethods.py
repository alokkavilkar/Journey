class Employee:

    salary = 100

    # def changeSalary(self, salary):
    #     self.salary = salary

    # to change class atrribute use classmethods;

    @classmethod
    def change_salary(cls, salary):
        cls.salary = salary

e = Employee()
print(e.salary)
e.change_salary(200)
print(e.salary)
print(Employee.salary)

# property decorator

class Emp:

    salary = 500
    bonu = 100

    def __init__(self) -> None:
        self.__x = None

    @property
    def increase(self):
        print(self.salary + self.bonu)

    @property
    def x(self):
        print(self.__x)

        

    @x.setter
    def x(self, value):
        self.__x =value

    @x.deleter
    def x(self):
        del self.__x






et = Emp()
et.increase
et.x 
et.x = 30
et.x
et.x
