# Change Boolean Object parameter with a method


class Car:
    def __init__(self, car_type, make):
        self.car_type = car_type
        self.make = make
        self.is_fuel = True

    def refuel(self):
        self.is_fuel = True

    def drive_till_stop(self):
        self.is_fuel = False

    def show_fuel(self):
        if self.is_fuel is True:
            return f"{self.make} has fuel."
        else:
            return f"{self.make} does not have fuel."


simon_car = Car("Family", "Mazda")
simon_car.drive_till_stop()
print(simon_car.show_fuel())
simon_car.refuel()
print(simon_car.show_fuel())
