"""
Design the following code:

     _____________________
     |                   |
     |      Vehicle      |
     |___________________|
     |                   |
     |+ color            |
     |___________________|
     |                   |
     |+ vehicleInfo()    |
     |___________________|
               ^
               |
     _____________________
     |                   |
     |       Taxi        |
     |___________________|
     |                   |
     |-- model           |
     |-- capacity        |
     |-- variant         |
     |___________________|
     |                   |
     |+ getModel()       |
     |+ getCapacity()    |
     |+ getVariant()     |
     |+ setModel()       |
     |+ setCapacity()    |
     |+ setVariant()     |
     |+ vehicleInfo()    |
     |___________________|   -> Create two instances (t1, t2)

"""

class Vehicle:
    def __init__(self, color):
        self.color = color

    def vehicleInfo(self):
        print(f"Vehicle Color: {self.color}")


class Taxi(Vehicle):
    def __init__(self, color, model, capacity, variant):
        super().__init__(color)
        self.__model = model
        self.__capacity = capacity
        self.__variant = variant

    def getModel(self):
        return self.__model

    def getCapacity(self):
        return self.__capacity

    def getVariant(self):
        return self.__variant

    def setModel(self, model):
        self.__model = model

    def setCapacity(self, capacity):
        self.__capacity = capacity

    def setVariant(self, variant):
        self.__variant = variant

    def vehicleInfo(self):
        super().vehicleInfo()
        print(f"Model: {self.__model}, Capacity: {self.__capacity}, Variant: {self.__variant}")


# Example usage
t1 = Taxi("Yellow", "Toyota Prius", 4, "Hybrid")
t2 = Taxi("White", "Honda Civic", 5, "Sedan")

t1.vehicleInfo()
t2.vehicleInfo()
