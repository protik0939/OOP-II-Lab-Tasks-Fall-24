"""

Do the following code:

                    _______________________
                    |                     |
                    |    << Vehicle >>    |
                    |_____________________|
                    |                     |
                    |                     |
                    |_____________________|
                    |                     |
                    |+ start()            |
                    |+ stop()             |
                    |_____________________|
                        ^             ^
                        |             |
                        |             |
                        |             |
                        |             | 
     ___________________|___        __|____________________
     |                     |        |                     |
     |         car         |        |      MotorCycle     |
     |_____________________|        |_____________________|
     |                     |        |                     |
     |                     |        |                     |
     |_____________________|        |_____________________| 
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started.")

    def stop(self):
        print("Car stopped.")


class MotorCycle(Vehicle):
    def start(self):
        print("Motorcycle started.")

    def stop(self):
        print("Motorcycle stopped.")


car = Car()
motorcycle = MotorCycle()

car.start()
car.stop()

motorcycle.start()
motorcycle.stop()

try:
    vehicle = Vehicle()
except TypeError as e:
    print(e)
