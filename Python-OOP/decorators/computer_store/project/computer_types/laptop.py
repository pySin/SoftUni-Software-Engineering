from project.computer_types.computer import Computer


class Laptop(Computer):

    @property
    def available_processors(self):
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }

    @property
    def max_ram(self):
        return 64

    def __str__(self):
        return "laptop"


# from project.computer_types.computer import Computer
#
#
# class Laptop(Computer):
#     possible_processors = {None: 0, "AMD Ryzen 9 5950X": 900, "Intel Core i9-11900H": 1050, "Apple M1 Pro": 1200}
#     possible_ram = [None, 2, 4, 8, 16, 32, 64]
#
#     def configure_computer(self, processor: str, ram: int):
#         self.processor = processor
#         self.price += self.possible_processors[self.processor]
#         self.ram = ram
#         i = 0
#         while True:
#             i += 1
#             if 2 ** i == self.ram:
#                 self.price += i * 100
#                 break
#             if 2 ** i > self.ram:
#                 print("Ram not found exit!")
#                 break
#         return f"Created {self.manufacturer} {self.model} with {self.processor} and " \
#                f"{self.ram}GB RAM for {self.price}$."
#
#     @property
#     def processor(self):
#         return self.__processor
#
#     @processor.setter
#     def processor(self, value):
#         if value not in self.possible_processors:
#             raise ValueError(f"{value} is not compatible with laptop "
#                              f"{self.manufacturer} {self.model}!")
#         self.__processor = value
#
#     @property
#     def ram(self):
#         return self.__ram
#
#     @ram.setter
#     def ram(self, value):
#         if value not in self.possible_ram:
#             raise ValueError(f"{value}GB RAM is not compatible with laptop "
#                              f"{self.manufacturer} {self.model}!")
#         self.__ram = value


# laptop1 = Laptop("Apple", "Macbook")
# print(laptop1)
# print(laptop1.configure_computer("Apple M1 Pro", 64))
