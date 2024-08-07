from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.user import User
from project.route import Route


class ManagingApp:
    VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    #helper
    def find_rout_by_start_and_end_point(self, start_point, end_point):
        route_check = [route for route in self.routes if route.start_point == start_point and route.end_point == end_point]
        if route_check:
            return route_check[0]
        return None

    #helper
    def create_route(self, start_point: str, end_point: str, length: float):
        number = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id=number)
        return new_route


    def register_user(self, first_name, last_name, driving_license_number):
        try:
            user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str ):
        if vehicle_type not in self.VEHICLE_TYPES.keys():
            return f"Vehicle type {vehicle_type} is inaccessible."

        try:
            vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
            return f"{license_plate_number} belongs to another vehicle."
        except StopIteration:
            new_vehicle = self.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
            self.vehicles.append(new_vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        found_route = self.find_rout_by_start_and_end_point(start_point, end_point)

        if found_route is not None:
            if found_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if found_route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if found_route.length > length:
                found_route.is_locked = True

        new_route = self.create_route(start_point, end_point, length)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda u: u.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count):
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        sorted_vehicles = sorted(damaged_vehicles, key=lambda a: (a.brand, a.model))[:count]

        for vehicle in sorted_vehicles:
            vehicle.is_damaged = False
            vehicle.recharge()

        return f"{len(sorted_vehicles)} vehicles were successfully repaired!"

    def users_report(self):

        sorted_users = sorted(self.users, key=lambda u: -u.rating)
        output = ["*** E-Drive-Rent ***"]

        output.append(('\n'.join(str(user) for user in sorted_users)))
        return '\n'.join(output)
