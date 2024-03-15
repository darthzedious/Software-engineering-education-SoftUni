from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @property
    @abstractmethod
    def air_cond_on(self):
        ...

    def drive(self, distance):
        consumation = (self.air_cond_on + self.fuel_consumption) * distance

        if self.fuel_quantity >= consumation:
            self.fuel_quantity -= consumation


    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    @property
    def air_cond_on(self):
        return 0.9

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    FULL_TANK = 0.95

    @property
    def air_cond_on(self):
        return 1.6

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.FULL_TANK


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)