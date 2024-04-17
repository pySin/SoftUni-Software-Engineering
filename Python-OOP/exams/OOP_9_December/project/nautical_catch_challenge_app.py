from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: list = []
        self.fish_list: list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        valid_diver_types = ["FreeDiver", "ScubaDiver"]

        if diver_type not in valid_diver_types:
            return f"{diver_type} is not allowed in our competition."

        already_registered = next((d for d in self.divers if d.name == diver_name), None)
        if already_registered:
            return f"{diver_name} is already a participant."

        if diver_type == "FreeDiver":
            self.divers.append(FreeDiver(diver_name))
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."
        elif diver_type == "ScubaDiver":
            self.divers.append(ScubaDiver(diver_name))
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        valid_types_of_fish = ["PredatoryFish", "DeepSeaFish"]
        if fish_type not in valid_types_of_fish:
            return f"{fish_type} is forbidden for chasing in our competition."

        already_added = next((f for f in self.fish_list if f.name == fish_name), None)
        if already_added:
            return f"{fish_name} is already permitted."

        if fish_type == "PredatoryFish":
            self.fish_list.append(PredatoryFish(fish_name, points))
            return f"{fish_name} is allowed for chasing as a {fish_type}."
        elif fish_type == "DeepSeaFish":
            self.fish_list.append(DeepSeaFish(fish_name, points))
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        valid_diver = next((d for d in self.divers if d.name == diver_name), None)
        if not valid_diver:
            return f"{diver_name} is not registered for the competition."

        valid_fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if not valid_fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if valid_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if valid_diver.oxygen_level < valid_fish.time_to_catch:
            valid_diver.miss(valid_fish.time_to_catch)
            # valid_diver.oxygen_level -= valid_fish.time_to_catch
            return f"{diver_name} missed a good {fish_name}."

        if valid_diver.oxygen_level == valid_fish.time_to_catch:
            if is_lucky:
                valid_diver.hit(valid_fish)
                return f"{diver_name} hits a {valid_fish.points}pt. {fish_name}."
            else:
                valid_diver.miss(valid_fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        valid_diver.hit(valid_fish)
        return f"{diver_name} hits a {valid_fish.points}pt. {fish_name}."

    def health_recovery(self):
        recovered_divers = 0
        for current_diver in self.divers:
            if current_diver.has_health_issue:
                recovered_divers += 1
                current_diver.has_health_issue = False
                current_diver.oxygen_level = current_diver.INITIAL_OXYGEN_LEVEL
        return f"Divers recovered: {recovered_divers}"

    def diver_catch_report(self, diver_name: str):
        current_diver = next((d for d in self.divers if d.name == diver_name), None)

        report = F"**{diver_name} Catch Report**\n"
        for fish in current_diver.catch:
            report += fish.fish_details() + "\n"
        return report[:-1]

    def competition_statistics(self):
        statistics = "**Nautical Catch Challenge Statistics**\n"

        healthy_divers = [d for d in self.divers if not d.has_health_issue]
        healthy_divers = sorted(healthy_divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        statistics += "\n".join([hd.__str__() for hd in healthy_divers])

        return statistics


nautical_catch_challenge = NauticalCatchChallengeApp()

# Dive into competition
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "MaxineHarper"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "JamalCarter"))
print(nautical_catch_challenge.dive_into_competition("SkyDiver", "FionaBennett"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "OscarWallace"))
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "LilaMoreno"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "LilaMoreno"))

# Swim into competition
print(nautical_catch_challenge.swim_into_competition("ReefFish", "AzureDamselfish", 8.7))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "BluestripeSnapper", 6.3))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "YellowtailSurgeonfish", 5.0))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Barracuda", 9.2))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Coryphaena", 9.7))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Bluefish", 4.4))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "SwordFish", 10.0))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Mahi-Mahi", 9.1))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Tuna", 8.5))
print(nautical_catch_challenge.swim_into_competition("AquariumFish", "SilverArowana", 3.3))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Barracuda", 8.6))

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("FionaBennett", "AzureDamselfish", False))
print(nautical_catch_challenge.chase_fish("JamalCarter", "SilverArowana", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Tuna", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Coryphaena", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "BluestripeSnapper", True))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Barracuda", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Tuna", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "Barracuda", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "YellowtailSurgeonfish", True))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# Check health recovery
print(nautical_catch_challenge.health_recovery())

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))


# View catch reports
print(nautical_catch_challenge.diver_catch_report("LilaMoreno"))

# View competition statistics
print(nautical_catch_challenge.competition_statistics())
