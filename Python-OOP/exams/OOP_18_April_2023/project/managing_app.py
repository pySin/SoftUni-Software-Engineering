from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    def __init__(self):
        self.users: list = []
        self.vehicles: list = []
        self.routes: list = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        already_registered_user = next((u for u in self.users if u.driving_license_number == driving_license_number)
                                       , None)
        if already_registered_user:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        valid_vehicles = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

        if vehicle_type not in valid_vehicles:
            return f"Vehicle type {vehicle_type} is inaccessible."

        already_registered_plate = next((p for p in self.vehicles if
                                         p.license_plate_number == license_plate_number), None)
        if already_registered_plate:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(valid_vehicles[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        # self, start_point: str, end_point: str, length: float, route_id: int

        route_already_registered = next((r for r in self.routes if
                                         r.start_point == start_point
                                         and r.end_point == end_point
                                         and r.length == length), None)
        if route_already_registered:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        route_already_registered = next((r for r in self.routes if
                                         r.start_point == start_point
                                         and r.end_point == end_point
                                         and r.length < length), None)
        if route_already_registered:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))

        route_already_registered = next((r for r in self.routes if
                                         r.start_point == start_point
                                         and r.end_point == end_point
                                         and r.length > length), None)
        if route_already_registered:
            route_already_registered.is_locked = True
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        # print([us.driving_license_number for us in self.users])
        user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        route = next((r for r in self.routes if r.route_id == route_id), None)
        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)

        # vehicle.drive(route.length)

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

        # vehicle.drive(route.length)

        return vehicle.__str__()
        # return f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number} " \
        #        f"Battery: {vehicle.battery_level}% Status: {vehicle.__str__()}"

    def repair_vehicles(self, count: int):
        damaged_vehicles = sorted([v for v in self.vehicles if v.is_damaged], key=lambda x: (x.brand, x.model))
        damaged_vehicles = damaged_vehicles if len(damaged_vehicles) < count else damaged_vehicles[:count]
        for vehicle in damaged_vehicles:
            vehicle.is_damaged = False
            vehicle.battery_level = 100
        return f"{len(damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        report = "*** E-Drive-Rent ***\n"
        users = sorted(self.users, key=lambda x: -x.rating)
        users_reports = "\n".join([user.__str__() for user in users])
        report += users_reports
        return report
