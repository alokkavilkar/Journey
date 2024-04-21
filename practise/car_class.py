class Pet:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} please sit')

    def roll_over(self):
        print(f'{self.name} please roll over.')

class Dog(Pet):

    def __init__(self, name: str, age: int, nickname:str) -> None:
        super().__init__(name, age)
        self.nickname = nickname

    

hubby = Pet('hubby', 20)
hubby.name = 'alok'
hubby.sit()

jin = Dog('jin', 20, 'jinu')
jin.sit()

class Car:

    def __init__(self) -> None:
        pass

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class Battery():

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class Electric(Car):

    def __init__(self) -> None:
        self.battery = Battery()


ele1 = Electric()
ele1.battery.describe_battery()

