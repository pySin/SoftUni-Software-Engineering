# class Car:
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def start_engine(self):
#         print(f"The {self.make} {self.model}\'s engine is starting")
#
#     def drive(self, distance):
#         print(f"The {self.make} {self.model}\' is driving {distance} kilometers")
#
#     def stop_engine(self):
#         print(f"The {self.make} {self.model}\'s engine is stopping")
#
#
# car1 = Car("Toyota", "Corolla", 2020)
# car2 = Car("Tesla", "Cybertruck", 2023)
# print(car1.model)
# print(car2.model)
#
# car2.start_engine()
# car2.drive(200)
# car2.stop_engine()


class Car:

    def set_model(self, model):
        self.model = model

    def set_color(self, color):
        self.color = color

    def display_info(self):
        print(f"Model: {self.model}, Color: {self.color}")


car = Car()
car.set_model("Toyota Prius")
car.set_color("Purple")
car.display_info()
