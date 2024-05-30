# ここにコードを書いてください
from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = int(year)

    def get_details(self):
        return f"Vehicle: {self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    
    def get_details(self):
        return f"Car: {self.year} {self.make} {self.model}"

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def get_details(self):
        return f"Truck: {self.year} {self.make} {self.model}, Towing Capacity: {self.towing_capacity}"


def display_vehicle_details(vehicle):
    # ここにコードを書いてください
    print(vehicle.get_details())


car = Car(make="Toyota", model="Corolla", year=2021)
truck = Truck(make="Ford", model="F-150", year=2020, towing_capacity=5000)

print(car.get_details())  # Car: 2021 Toyota Corolla
print(truck.get_details())  # Truck: 2020 Ford F-150, Towing Capacity: 5000

display_vehicle_details(car)  # Car: 2021 Toyota Corolla
display_vehicle_details(truck)  # Truck: 2020 Ford F-150, Towing Capacity: 5000