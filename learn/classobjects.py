class Cars :
    # class attributes
    wheels = 4
    
    def __init__(self, body):
        # instance attributes
        print("This method is called first.")
        self.body = body
        
    def methods(self):
        print(f"{self.body} has a body with wheels {Myclass.wheels} from {self}")
        

car = Cars('petrol')
# if we change class attribute for instance of object only it will change.
# if class change attributes then all must follow.
Myclass.wheels = 5
car.wheels = 10
print(car.wheels) # 10
print(Cars.wheels) # 5
newcar = Cars('diesal')
print(newcar.wheels) # 5
print(Cars.wheels) # 5
car.methods()


# --------------------------------- Self Keyword ---------------------------------
class Employee:
    company = 'google'
    
    def __init__(self):
        self.status ='online'
    
    def getData(self):
        print(self)
        return 10
        
    @classmethod
    def changeCompany(cls):
        # self.status = 'offline' can't access instance attributes
        cls.company = 'tata'
        
    @staticmethod
    def formatCurrency(ruppess):
        return "{:,.2f}".format(ruppess)
        
alok = Employee()
# alok.getData() returns with error like takes 0 argument but one was given
'''
alok.getData()
it's getting converted into Employee.getData(alok)
so alok parameter is handled by self
self is object instance atrributes accessor.
'''
alok.getData()
print(alok.company)
alok.changeCompany()
print(alok.company, Employee.company)
print(alok.formatCurrency(100))
print(Employee.formatCurrency(1000))


# ----------------- practical use case of classmethods -----------------
class Myclass:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
        
c = Myclass(2021, 4, 30)
c.from_string("2020-05-30")
print(c.year)

# it will return a object as called with __init__ method.
date = Myclass.from_string("2003-03-07")
print(date.year)


# ----------------------------------------------------------------------------




