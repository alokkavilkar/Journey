class Animal:

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method.")
    

class Dog(Animal):

    def print_info(self):
        print(f'{self.name}')
    
    def speak(self):
        return f'{self.name} says Woof'
    

class Cat(Animal):

    def speak(self):
        return f'{self.name} says meow.'
    

dog = Dog("Buddy")
dog.print_info()
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())

