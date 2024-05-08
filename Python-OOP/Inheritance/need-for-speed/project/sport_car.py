from car import Car


class SportCar(Car):
    fuel_consumption = 10
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)


