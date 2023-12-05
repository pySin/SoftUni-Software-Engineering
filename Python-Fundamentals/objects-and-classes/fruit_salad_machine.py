# Fruit Salad Machine

class FruitSaladMachine:

    apple_weight_loose = 8
    banana_weight_loose = 7
    strawberry_weight_loose = 5
    priority_fruit = ["apple", "banana", "strawberry"]

    def __init__(self, salad_size):
        self.salad_size = salad_size

    def apple_loss(self, percent):
        self.apple_weight_loose = percent

    def banana_loss(self, percent):
        self.banana_weight_loose = percent

    def strawberry_loss(self, percent):
        self.strawberry_weight_loose = percent

    def fruits_priority(self, priority):
        priority = priority.split(", ")
        self.priority_fruit = priority

    def make_salad(self, fruits_weight):  # apple: 85, banana: 110, strawberry: 6
        fruits_weight = fruits_weight.split(", ")
        apple_in_salad = int(fruits_weight[0].split()[1]) * (1 - (self.apple_weight_loose / 100))
        banana_in_salad = int(fruits_weight[1].split()[1]) * (1 - (self.banana_weight_loose / 100))
        strawberry_in_salad = int(fruits_weight[2].split()[1]) * (1 - (self.strawberry_weight_loose / 100))

        apples_in_salad = 0
        bananas_in_salad = 0
        strawberries_in_salad = 0
        current_salad_size = 0

        is_salad_enough = False
        while True:
            for fruit in self.priority_fruit:
                if fruit == "apple":
                    if current_salad_size >= self.salad_size:
                        is_salad_enough = True
                        break
                    else:
                        apples_in_salad += 1
                        current_salad_size += apple_in_salad

                if fruit == "banana":
                    if current_salad_size >= self.salad_size:
                        is_salad_enough = True
                        break
                    else:
                        bananas_in_salad += 1
                        current_salad_size += banana_in_salad

                if fruit == "strawberry":
                    if current_salad_size >= self.salad_size:
                        is_salad_enough = True
                        break
                    else:
                        strawberries_in_salad += 1
                        current_salad_size += strawberry_in_salad

            if is_salad_enough:
                break

        return f"You made a salad weighing {current_salad_size:.2f} with {apples_in_salad} apples, " \
               f"{bananas_in_salad} bananas and {strawberries_in_salad} strawberries."


machine = FruitSaladMachine(375)
print(machine.make_salad("apple: 85, banana: 110, strawberry: 6"))
machine.fruits_priority("strawberry, apple, banana")  # "apple", "banana", "strawberry"
print(machine.make_salad("apple: 85, banana: 110, strawberry: 6"))
machine.apple_loss(12)
print(machine.make_salad("apple: 85, banana: 110, strawberry: 6"))
