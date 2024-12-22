"""
     _____________________
     |                   |
     |      Shape        |
     |___________________|
     |                   |
     |- name             |
     |___________________|
     |                   |
     |+ getName          |
     |___________________|
     |                   |
     |+ display()        |
     |display_Info()     |
     |___________________|
               ^
               |     
     _____________________
     |                   |
     |      Rectangle    |
     |___________________|
     |                   |
     |-- length          |
     |-- width           |
     |___________________|
     |                   |
     |+ area()           |
     |+ perimeter()      |
     |___________________|
               
"""

class Shape:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def display(self):
        print(f"Shape Name: {self.name}")


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_Info(self):
        print(f"Rectangle Name: {self.getName()}")
        print(f"Length: {self.length}, Width: {self.width}")
        print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")


# Example usage
rect = Rectangle("MyRectangle", 10, 5)
rect.display_Info()
