from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Usage
circle = Circle(5)
print("Circle Area:", circle.area())        # Output: Circle Area: 78.5
print("Circle Perimeter:", circle.perimeter())  # Output: Circle Perimeter: 31.400000000000002

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())     # Output: Rectangle Area: 24
print("Rectangle Perimeter:", rectangle.perimeter())  # Output: Rectangle Perimeter: 20
