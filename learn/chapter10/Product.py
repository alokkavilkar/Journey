# Question 1: 

# You are tasked with designing a simple inventory management system for a retail store. Implement a Python class Product to represent products in the inventory. Each product has a name, price, and quantity. Implement the following functionalities:

# Add a static method calculate_total_cost in the Product class that calculates the total cost of purchasing a certain quantity of a product, given its price.
# Create an instance of the Product class for a product named "Laptop" with a price of $1000 and a quantity of 5. Use the calculate_total_cost method to calculate the total cost of purchasing 3 laptops.

class Product:
    store = 'Jai Maha'
    gst = 0.18
    _no_count = 0


    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.increase_count()

    @staticmethod
    def gst_rate(gst, price):
        return gst * price
    
    def get_receipt(self):
        print(f"{self.name} with {self.quantity} got price of {Product.calculate_total_cost(self.quantity, self.price, self.gst)}")

    @staticmethod
    def calculate_total_cost(quantity, price, gst):
        return quantity * price + Product.gst_rate(price, gst)
    
    @staticmethod
    def increase_count():
        Product._no_count += 1
        
    

laptop = Product('Dell', 10000, 5)
laptop.get_receipt()
print(Product.gst)
print(laptop.gst)
# laptop.increase_count()
# Real use case of static method is that its access and shared location or variable.
print(laptop.gst, Product.gst)
print(laptop._no_count, Product._no_count)
new_oops = Product('Dell', 20000, 6)
print(new_oops.gst)
print(laptop._no_count, Product._no_count)

