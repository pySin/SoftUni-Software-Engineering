from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths: list = []
        self.delicacies: list = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        valid_delicacies = {"Gingerbread": Gingerbread, "Stolen": Stolen}

        if next((d for d in self.delicacies if d.name == name), None):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in valid_delicacies:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(valid_delicacies[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth_types = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

        if next((b for b in self.booths if b.booth_number == booth_number), None):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in booth_types:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(booth_types[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        available_booth = next((b for b in self.booths if b.capacity >= number_of_people), None)

        if not available_booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        available_booth.reserve(number_of_people)
        return f"Booth {available_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)

        booth_bill = booth.price_for_reservation + (sum([d.price for d in booth.delicacy_orders]))
        self.income += booth_bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0.0

        return f"Booth {booth.booth_number}:\nBill: {booth_bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
