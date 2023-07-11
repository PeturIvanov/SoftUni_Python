from typing import List

from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[CargoVan or PassengerCar] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        driving_licenses = [user.driving_license_number for user in self.users]

        if driving_license_number in driving_licenses:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."

        plates_numbers = [vehicle.license_plate_number for vehicle in self.vehicles]

        if license_plate_number in plates_numbers:
            return f"{license_plate_number} belongs to another vehicle."

        if vehicle_type == "PassengerCar":
            self.vehicles.append(PassengerCar(brand, model, license_plate_number))

        else:
            self.vehicles.append(CargoVan(brand, model, license_plate_number))

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if start_point == route.start_point and end_point == route.end_point and length == route.length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if start_point == route.start_point and end_point == route.end_point:
                if route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."

                else:
                    route.is_locked = True
                    break

        self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self,driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user: User = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle: CargoVan or PassengerCar = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        route: Route = [r for r in self.routes if r.route_id == route_id][0]

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

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))
        count_repaired_vehicles = 0

        for idx in range(count):
            try:
                current_car = sorted_vehicles[idx]
                current_car.is_damaged = False
                current_car.recharge()
                count_repaired_vehicles += 1
            except IndexError:
                break

        return f"{count_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: -x.rating)

        result = "*** E-Drive-Rent ***\n"
        result += ("\n".join([str(u) for u in sorted_users]))

        return result
