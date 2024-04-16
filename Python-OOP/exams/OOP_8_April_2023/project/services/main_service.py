from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        information = f"{self.name} Main Service:\n"
        robots = " ".join([r.name for r in self.robots])
        information = information + "Robots: " + robots if robots else information + "Robots: none"
        return information




