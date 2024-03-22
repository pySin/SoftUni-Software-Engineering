class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return "Skill already added"

    def player_info(self):
        player_information = ""
        player_information += f"Name: {self.name}\n"
        player_information += f"Guild: {self.guild}\n"
        player_information += f"HP: {self.hp}\n"
        player_information += f"MP: {self.mp}\n"
        player_information += "\n".join([f"==={skill} - {mana}" for skill, mana in self.skills.items()])
        return player_information + "\n"
