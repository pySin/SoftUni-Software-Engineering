from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    TIME_TO_CATCH = 180

    def __init__(self, name: str, points: float):
        super().__init__(name, points, self.TIME_TO_CATCH)

    def fish_details(self):
        return f"{self.__class__.__name__}: {self.name} [Points: {self.points}, Time to Catch:" \
               f" {self.time_to_catch} seconds]"


# dsf = DeepSeaFish("Kostur", 8)
# print(dsf.__dict__)
# print(dsf.fish_details())
