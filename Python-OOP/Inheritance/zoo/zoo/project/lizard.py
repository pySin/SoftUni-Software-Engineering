from reptile import Reptile


class Lizard(Reptile):
    def __init__(self, name: str):
        super().__init__(name)


f = Lizard("Froggy")
print(f.__class__.__bases__[0].__bases__[0].__name__)
