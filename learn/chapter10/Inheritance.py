class Employee:
    company = 'google'
    
    def get_name(self):
        print(f'{self.name} is name')

    def take_breadth(self):
        print("I'm breadthing......")


class Employee2(Employee):

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name


    def take_breadth(self):
        super().take_breadth()
        print("I'm breadthing too.......")

e = Employee()
# e.name = 'Mahesh'
# e.get_name()
e.take_breadth()
e1 = Employee2('Rahul')
# e1.get_name()
e1.take_breadth()