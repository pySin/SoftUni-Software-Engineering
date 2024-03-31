# Vehicle


class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


car = Vehicle(max_speed=100, mileage=25)
print(car.max_speed)
print(car.mileage)
