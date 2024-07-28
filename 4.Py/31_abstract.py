'''
    - Prevents a user from creating an object of the class 
    - Compels a user to override abstract methods in child class
    - Class which contains one or more abstract methods
    - Abstract method - which has declaration but not an implementation
'''

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car.")

    def stop(self):
        print("This car is stopped")

class Motorcyle(Vehicle):
    def go(self):
        print("You ride the motorcycle.")

    def stop(self):
        print("This motorcycle is stopped")

car = Car()
car.go()
car.stop()

motorcycle = Motorcyle()
motorcycle.go()
motorcycle.stop()