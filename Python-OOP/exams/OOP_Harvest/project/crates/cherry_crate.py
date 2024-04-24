from project.crates.base_crate import BaseCrate


class CherryCrate(BaseCrate):
    WEIGHT_WHEN_FULL = 5.8

    def __init__(self, size: str, color: str):
        super().__init__(size, color, self.WEIGHT_WHEN_FULL)

    def calculate_weight(self):
        weight = self.degree_of_fullness * (self.weight_when_full / 100)
        return weight
