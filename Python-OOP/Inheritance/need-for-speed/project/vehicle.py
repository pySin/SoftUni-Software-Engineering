class Vehicle:

    DEFAULT_FUEL_CONSUMPTION = 13

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = 1.25
        Vehicle.DEFAULT_FUEL_CONSUMPTION = self.fuel_consumption

    def drive(self, kilometers):
        if self.DEFAULT_FUEL_CONSUMPTION * kilometers <= self.fuel:
            self.fuel -= self.DEFAULT_FUEL_CONSUMPTION * kilometers
