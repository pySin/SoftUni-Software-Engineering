from product import Product


class Drink(Product):
    def __init__(self, name: str):
        self.name = name
        self.quantity = 10
        super().__init__(self.name, self.quantity)
