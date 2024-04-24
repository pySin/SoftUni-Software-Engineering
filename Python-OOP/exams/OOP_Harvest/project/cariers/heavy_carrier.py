from project.cariers.base_carrier import BaseCarrier


class HeavyCarrier(BaseCarrier):
    BATTERY_CAPACITY = 120
    KILOMETERS_PER_BATTERY_UNIT = 3.0

    def __init__(self, max_weight: float):
        super().__init__(max_weight, self.BATTERY_CAPACITY, self.KILOMETERS_PER_BATTERY_UNIT)

    def distance_left(self):
        return self.KILOMETERS_PER_BATTERY_UNIT * (self.BATTERY_CAPACITY * (self.remaining_battery / 100))
