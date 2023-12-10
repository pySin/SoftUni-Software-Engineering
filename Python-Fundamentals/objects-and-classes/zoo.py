# Zoo


class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
            self.__animals += 1
        elif species == "fish":
            self.fishes.append(name)
            self.__animals += 1
        elif species == "bird":
            self.birds.append(name)
            self.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            mammal_names = ", ".join(self.mammals)
            print(f"Mammals in {self.name}: {mammal_names}")
        elif species == "fish":
            fishes_names = ", ".join(self.fishes)
            print(f"Fishes in {self.name}: {fishes_names}")
        elif species == "bird":
            birds_names = ", ".join(self.birds)
            print(f"Birds in {self.name}: {birds_names}")

        print(f"Total animals: {self.__animals}")


def call_functions():
    zoo_name = Zoo(input())
    animals_to_add = int(input())

    for _ in range(animals_to_add):
        animal = input().split()
        zoo_name.add_animal(animal[0], animal[1])

    species = input()
    zoo_name.get_info(species)


if __name__ == "__main__":
    call_functions()
