from abc import ABC, abstractmethod


class BaseCrate(ABC):

    def __init__(self, size: str, color: str, weight_when_full: float):
        self.size = size
        self.color = color
        self.weight_when_full: float = weight_when_full
        self.degree_of_fullness: float = 0.0
        self.is_collection_ready: bool = False

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value.strip() == "":
            raise ValueError("Size can not be empty!")
        elif value not in ['small', 'medium', 'big']:
            raise ValueError("Sizes can be only small, medium and big!")
        self.__size = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        valid_colors = ["red", "green"]
        if value not in valid_colors:
            raise ValueError("Colors can be only red and green!")
        self.__color = value

    @property
    def degree_of_fullness(self):
        return self.__degree_of_fullness

    @degree_of_fullness.setter
    def degree_of_fullness(self, value):
        if value >= 75:
            self.is_collection_ready = True
        elif 0 <= value < 75:
            self.is_collection_ready = False
        else:
            raise ValueError("A crate can't be negatively full!")
        self.__degree_of_fullness = value

    @property
    @abstractmethod
    def calculate_weight(self):
        pass

