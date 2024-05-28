from vehicle import Vehicle
import csv

def parse_vehicle_data(file_path) -> list:
    vehicles = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            vehicles.append(Vehicle(*row))
    return vehicles
