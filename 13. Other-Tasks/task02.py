"""
Do the following code:

                    _______________________
                    |                     |
                    |    << Vehicle >>    |
                    |_____________________|
                    |                     |
                    |+ brand              |
                    |_____________________|
                    |                     |
                    |+ startEngine()      | -> abstract method
                    |+ description()      | -> non-abstryct method
                    |_____________________|
                               ^
                               |
                               |
                               |
                               | 
                    ___________|___________
                    |                     |
                    |         car         |
                    |_____________________|
                    |                     |
                    |+model               |
                    |_____________________|
                    
Create an object of car. What will happen if we try to create an object of Vehicles class?

"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def startEngine(self):
        pass

    def description(self):
        print(f"This is a vehicle of brand: {self.brand}")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def startEngine(self):
        print(f"{self.brand} {self.model} engine started.")

    def description(self):
        super().description()
        print(f"The model is: {self.model}")


car = Car("Toyota", "Corolla")
car.startEngine()
car.description()

try:
    vehicle = Vehicle("Generic Brand")
except TypeError as e:
    print(e)
