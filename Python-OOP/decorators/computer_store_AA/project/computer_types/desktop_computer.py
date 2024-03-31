from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    @property
    def available_processors(self):
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }

    @property
    def max_ram(self):
        return 128

    def __str__(self):
        return "desktop computer"



# from project.computer_types.computer import Computer
#
#
# class DesktopComputer(Computer):
#     possible_processors = {None: 0, "AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}
#     possible_ram = [None, 2, 4, 8, 16, 32, 64, 128]
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
#         return f"Created {self.manufacturer} {self.model} with {self.processor } and " \
#                f"{self.ram}GB RAM for {self.price}$."
#
#     @property
#     def processor(self):
#         return self.__processor
#
#     @processor.setter
#     def processor(self, value):
#         if value not in self.possible_processors:
#             raise ValueError(f"{value} is not compatible with desktop computer "
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
#             raise ValueError(f"{value}GB RAM is not compatible with desktop computer "
#                              f"{self.manufacturer} {self.model}!")
#         self.__ram = value


# dc = DesktopComputer("Apple", "Macbook")
# print(dc.configure_computer("Apple M1 Max", 128))
