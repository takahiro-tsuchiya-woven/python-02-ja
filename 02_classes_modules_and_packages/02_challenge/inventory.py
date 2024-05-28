from vehicle import Vehicle
import re
    
class Inventory:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle) -> None:
        self.vehicles.append(vehicle)
    
    def retrieve_vehicles(self):
        return self.vehicles
    # def add_vehicle(self, obj):
    #     self.vehicles.append(Vehicle(**obj))
    
    def apply_discount(self, condition, discount) -> None:
        # new_vehicles = []
        # for vehicle in self.vehicles:
        #     if condition(vehicle):
        #         vehicle["discount"] = discount
        
        # self.vehicles = [Vehicle(
        #                     v.model,
        #                     v.make,
        #                     v.year,
        #                     v.price,
        #                     discount if condition(v) else v.discount
        #                 ) for v in self.vehicles]
        for vehicle in self.vehicles:
            if condition(vehicle):
                vehicle.set_discount(discount)
        
    def search_vehicles(self, pattern) -> list:
        # return [v for v in self.vehicles if re.search(pattern, v.model)]
        return [v for v in self.vehicles if re.search(pattern, v.model) is not None]
    
    def generator(self):
        for vehicle in self.vehicles:
            yield vehicle
