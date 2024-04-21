from typing import List
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers: list = []
        self.peaks: list = []

    def register_climber(self, climber_type: str, climber_name: str):
        is_name_found = next((c for c in self.climbers if c.name == climber_name), None)
        if is_name_found:
            return f"{climber_name} has been already registered."

        if climber_type == "ArcticClimber":
            self.climbers.append(ArcticClimber(climber_name))
            return f"{climber_name} is successfully registered as a {climber_type}."
        elif climber_type == "SummitClimber":
            self.climbers.append(SummitClimber(climber_name))
            return f"{climber_name} is successfully registered as a {climber_type}."
        else:
            return f"{climber_type} doesn't exist in our register."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in ["ArcticPeak", "SummitPeak"]:
            return f"{peak_type} is an unknown type of peak."

        if peak_type == "ArcticPeak":
            self.peaks.append(ArcticPeak(peak_name, peak_elevation))
            return f"{peak_name} is successfully added to the wish list as a {peak_type}."
        elif peak_type == "SummitPeak":
            self.peaks.append(SummitPeak(peak_name, peak_elevation))
            return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = next((c for c in self.climbers if c.name == climber_name), None)
        peak = next((p for p in self.peaks if p.name == peak_name), None)
        gear_needed = peak.get_recommended_gear()
        missing_gear = [g for g in gear_needed if g not in gear]

        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: " \
                   f"{', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = next((c for c in self.climbers if c.name == climber_name), None)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = next((p for p in self.peaks if p.name == peak_name), None)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        # climber.climb(peak)
        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        elif not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."
        else:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        quest_statistics = f"Total climbed peaks: {len(self.peaks)}\n**Climber's statistics:**\n"
        for current_climber in self.climbers:
            current_climber.conquered_peaks = sorted(current_climber.conquered_peaks)
        successful_climbers = [c for c in self.climbers if len(c.conquered_peaks) > 0]
        sorted_climbers = sorted(successful_climbers, key=lambda x: (-len(x.conquered_peaks), x.name))

        quest_statistics += "\n".join([s.__str__() for s in sorted_climbers])

        return quest_statistics


climbing_app = SummitQuestManagerApp()

# Register climbers
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Bob"))
print(climbing_app.register_climber("ExtremeClimber", "Dave"))
print(climbing_app.register_climber("ArcticClimber", "Charlie"))
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Eve"))
print(climbing_app.register_climber("SummitClimber", "Frank"))

# Add peaks to the wish list
print(climbing_app.peak_wish_list("ArcticPeak", "MountEverest", 4000))
print(climbing_app.peak_wish_list("SummitPeak", "K2", 3000))
print(climbing_app.peak_wish_list("ArcticPeak", "Denali", 2500))
print(climbing_app.peak_wish_list("UnchartedPeak", "MysteryMountain", 2000))

# Prepare climbers for climbing
print(climbing_app.check_gear("Alice", "MountEverest", ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]))
print(climbing_app.check_gear("Bob", "K2", ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]))
print(climbing_app.check_gear("Charlie", "Denali", ["Ice axe", "Crampons"]))

# Perform climbing
print(climbing_app.perform_climbing("Alice", "MountEverest"))
print(climbing_app.perform_climbing("Bob", "K2"))
print(climbing_app.perform_climbing("Kelly", "Denali"))
print(climbing_app.perform_climbing("Alice", "K2"))
print(climbing_app.perform_climbing("Alice", "MysteryMountain"))
print(climbing_app.perform_climbing("Eve", "MountEverest"))
print(climbing_app.perform_climbing("Charlie", "MountEverest"))
print(climbing_app.perform_climbing("Frank", "K2"))
print(climbing_app.perform_climbing("Frank", "Denali"))
print(climbing_app.perform_climbing("Frank", "MountEverest"))

# Get statistics
print(climbing_app.get_statistics())
