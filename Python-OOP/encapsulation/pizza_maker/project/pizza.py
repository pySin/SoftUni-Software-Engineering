from dough import Dough
from topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: dict[Topping.topping_type, Topping.weight] = {}
        # self.double_toppings = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough):
        if dough is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = dough

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.max_number_of_toppings:  # + self.double_toppings / after len maybe
            raise ValueError("Not enough space for another topping")

        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
            # self.double_toppings += 1
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        toppings_weight = sum([weight for key, weight in self.toppings.items()])

        return self.dough.weight + toppings_weight

