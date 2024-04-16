from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        information = f"{self.name} Secondary Service:\n"
        robots = " ".join([r.name for r in self.robots])
        information = information + "Robots: " + robots if robots else information + "Robots: none"
        return information


