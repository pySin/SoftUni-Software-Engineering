from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list = []
        self.teams: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # for symbol in value:
        #     if not symbol.isalnum():
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        valid_equipment_types = ["KneePad", "ElbowPad"]
        if equipment_type not in valid_equipment_types:
            raise Exception("Invalid equipment type!")

        if equipment_type == "KneePad":
            current_equipment = KneePad()
            self.equipment.append(current_equipment)
            return f"{equipment_type} was successfully added."
        elif equipment_type == "ElbowPad":
            current_equipment = ElbowPad()
            self.equipment.append(current_equipment)
            return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        valid_team_types = ["OutdoorTeam",  "IndoorTeam"]
        if team_type not in valid_team_types:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        if team_type == "OutdoorTeam":
            current_team = OutdoorTeam(team_name, country, advantage)
            self.teams.append(current_team)
            return f"{team_type} was successfully added."
        elif team_type == "IndoorTeam":
            current_team = IndoorTeam(team_name, country, advantage)
            self.teams.append(current_team)
            return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team_shopping = next((t for t in self.teams if t.name == team_name), None)
        if equipment_type == "KneePad":
            if KneePad.PRICE > team_shopping.budget:
                raise Exception("Budget is not enough!")
        elif equipment_type == "ElbowPad":
            if ElbowPad.PRICE > team_shopping.budget:
                raise Exception("Budget is not enough!")

        for i in range(len(self.equipment) - 1, - 1, - 1):
            if self.equipment[i].__class__.__name__ == equipment_type:
                # print("Equipment name: " + self.equipment[i].__class__.__name__ + f"{i}")
                team_shopping.budget -= self.equipment[i].price
                team_shopping.equipment.append(self.equipment.pop(i))
                # print(f"Show team equipment: {str(team_shopping.equipment)} Budget: {team_shopping.budget}")
                # print(f"{team_shopping.equipment}")
                return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        registered_team = next((t for t in self.teams if t.name == team_name), None)
        if not registered_team:
            raise Exception("No such team!")

        if registered_team.wins > 0:
            raise Exception(f"The team has {registered_team.wins} wins! Removal is impossible!")

        self.teams.remove(registered_team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0
        for equipment_modify in self.equipment:
            if equipment_modify.__class__.__name__ == equipment_type:
                # print(equipment_modify.price)
                equipment_modify.increase_price()
                # print(equipment_modify.price)
                number_of_changed_equipment += 1
        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = next((t1 for t1 in self.teams if t1.name == team_name1), None)
        team_2 = next((t2 for t2 in self.teams if t2.name == team_name2), None)
        # print(team_1.__class__.__name__)
        # print(team_2.__class__.__name__)

        if team_1.__class__.__name__ != team_2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team_1_strength = team_1.advantage + sum([e1.protection for e1 in team_1.equipment])
        team_2_strength = team_2.advantage + sum([e2.protection for e2 in team_2.equipment])

        if team_1_strength == team_2_strength:
            return "No winner in this game."

        winning_team = team_1 if team_1_strength > team_2_strength else team_2
        winning_team.win()
        return f"The winner is {winning_team.name}."

    def get_statistics(self):
        stats_info = f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n"
        self.teams = sorted(self.teams, key=lambda x: -x.wins)
        for team in self.teams:
            stats_info += team.get_statistics()

        return stats_info[:-1]



