from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots: list = []
        self.services: list = []

    def add_service(self, service_type: str, name: str):
        valid_service_types = {"MainService": MainService, "SecondaryService": SecondaryService}

        if service_type not in valid_service_types:
            raise Exception("Invalid service type!")

        self.services.append(valid_service_types[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        valid_robot_types = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

        if robot_type not in valid_robot_types:
            raise Exception("Invalid robot type!")

        self.robots.append(valid_robot_types[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next((r for r in self.robots if r.name == robot_name), None)
        service = next((s for s in self.services if s.name == service_name), None)

        appropriate_services = {"MaleRobot": "MainService", "FemaleRobot": "SecondaryService"}
        if not appropriate_services[robot.__class__.__name__] == service.__class__.__name__:
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(self.robots.pop(self.robots.index(robot)))
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next((s for s in self.services if s.name == service_name), None)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if not robot:
            raise Exception("No such robot in this service!")

        self.robots.append(service.robots.pop(service.robots.index(robot)))
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next((s for s in self.services if s.name == service_name), None)

        for service_robot in service.robots:
            service_robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = next((s for s in self.services if s.name == service_name), None)

        all_robots_price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {all_robots_price:.2f}."

    def __str__(self):
        service_reports = []
        for service in self.services:
            service_reports.append(service.details())
        return "\n".join(service_reports)

