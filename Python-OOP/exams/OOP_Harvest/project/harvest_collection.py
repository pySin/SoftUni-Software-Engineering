from project.crates.apple_crate import AppleCrate
from project.crates.cherry_crate import CherryCrate


class HarvestCollection:

    def __init__(self):
        self.crates: list = []
        self.carriers: list = []

    def add_crate(self, crate_type: str, size: str, color: str):
        crates_available = {"AppleCrate": AppleCrate, "CherryCrate": CherryCrate}
        self.crates.append(crates_available[crate_type](size, color))

    def load_crate(self, crate_type: str, percentages: int):
        current_crate = next((c for c in self.crates if c.__class__.__name__ == crate_type and
                              c.degree_of_fullness + percentages <= 100), None)

        if not current_crate:
            raise Exception("No suitable crate found for the load!")

        current_crate.degree_of_fullness += percentages


hc = HarvestCollection()
hc.add_crate("AppleCrate", "medium", "green")
hc.add_crate("CherryCrate", "small", "red")
hc.load_crate("CherryCrate", 20)
hc.load_crate("CherryCrate", 20)
for crate in hc.crates:
    print(crate.degree_of_fullness)
    print(crate.calculate_weight())
