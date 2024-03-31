from typing import List
from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profit = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        possible_computers = ["Desktop Computer", "Laptop"]
        if type_computer not in possible_computers:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        elif type_computer == possible_computers[0]:
            d_computer = DesktopComputer(manufacturer, model)
            comp_cre_expression = d_computer.configure_computer(processor, ram)
            self.warehouse.append(d_computer)
            return comp_cre_expression
        elif type_computer == possible_computers[1]:
            l_computer = Laptop(manufacturer, model)
            lap_cre_expression = l_computer.configure_computer(processor, ram)
            self.warehouse.append(l_computer)
            return lap_cre_expression

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for current_computer in self.warehouse:
            if current_computer.price <= client_budget and current_computer.processor == wanted_processor\
                    and current_computer.ram >= wanted_ram:
                self.profit += client_budget - current_computer.price
                return f"{current_computer} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")


