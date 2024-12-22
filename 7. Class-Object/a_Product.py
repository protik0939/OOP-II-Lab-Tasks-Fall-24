"""
     _____________________
     |                   |
     |      Product      |
     |___________________|
     |                   |
     |name               |
     |price              |
     |___________________|
     |                   |
     |display_detail()   | ->(Print name and price)
     |___________________|
               ^
               |     
     _____________________
     |                   |
     |Electronic_Product |
     |___________________|
     |                   |
     |warranty           |
     |___________________|
     |                   |
     |display_detail()   |
     |___________________|
               
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_detail(self):
        print(f"Product Name: {self.name}, Price: {self.price}")


class Electronic_Product(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_detail(self):
        super().display_detail()
        print(f"Warranty: {self.warranty} years")


# Example usage
product = Product("Generic Item", 100)
product.display_detail()

electronic_product = Electronic_Product("Laptop", 1000, 2)
electronic_product.display_detail()
