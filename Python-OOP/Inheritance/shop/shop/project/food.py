from product import Product


class Food(Product):
    def __init__(self, name: str):
        self.name = name
        self.quantity = 15
        super().__init__(self.name, self.quantity)


