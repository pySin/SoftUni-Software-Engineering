from abc import ABC, abstractmethod


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, value):
        # if len(value.strip("_")) < 2:
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        name = f"Name: {self.name}"
        country = f"Country: {self.country}"
        advantage = f"Advantage: {self.advantage} points"
        budget = f"Budget: {self.budget:.2f}EUR"
        wins = f"Wins: {self.wins}"
        all_prices = sum([p.price for p in self.equipment])
        total_equipment_price = f"Total Equipment Price: {all_prices:.2f}"
        avg_team_protection = sum([ep.protection for ep in self.equipment]) / len(self.equipment) \
            if len(self.equipment) != 0 else 0
        average_protection = f"Average Protection: {int(avg_team_protection)}\n"

        team_info = "\n".join([name, country, advantage, budget, wins, total_equipment_price, average_protection])
        return team_info
