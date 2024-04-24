from abc import ABC, abstractmethod


class BaseCarrier(ABC):

    def __init__(self, max_weight: float, battery_capacity: float, kilometers_per_battery_unit: float):
        self.max_weight = max_weight
        self.battery_capacity = battery_capacity
        self.remaining_battery: float = 100.0
        self.kilometers_per_battery_unit = kilometers_per_battery_unit

    @property
    def max_weight(self):
        return self.__max_weight

    @max_weight.setter
    def max_weight(self, value):
        if value < 30:
            raise ValueError("Load les than 30 is ineffective!")
        self.__max_weight = value

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value):
        if value < 50:
            raise ValueError("Capacity less than 50 in ineffective")
        self.__battery_capacity = value

    @property
    def remaining_battery(self):
        return self.__remaining_battery

    @remaining_battery.setter
    def remaining_battery(self, value):
        if value < 0:
            raise ValueError("Battery fullness can't be negative!")
        elif value > 100:
            raise ValueError("Battery can't be more than 100% full")
        self.__remaining_battery = value

    @property
    @abstractmethod
    def distance_left(self):
        pass
