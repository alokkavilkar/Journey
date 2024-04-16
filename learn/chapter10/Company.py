class Employee:

    company = "google"

    __rate = 10

    def __init__(self, name, unit, year_of_joining) -> None:
        self.name = name
        self.unit = unit
        self.year = year_of_joining

    def print_info(self):
        print(f'{self.name} works in {self.company} with unit {self.unit}')

    @staticmethod
    def no_of_employees(__rate):
        return __rate

    
employ1 = Employee('Ramesh', 'youtube', 2020)
print(employ1.company)
print(employ1.no_of_employees(2))
Employee.print_info(employ1)


