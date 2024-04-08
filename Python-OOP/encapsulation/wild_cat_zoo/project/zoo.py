# from lion import Lion
# from tiger import Tiger
# from cheetah import Cheetah
# from worker import Worker
# from vet import Vet


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals: list = []
        self.workers: list = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        else:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_salaries = 0
        for worker in self.workers:
            all_salaries += worker.salary
        if self.__budget >= all_salaries:
            self.__budget -= all_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        all_animals_care = 0
        for animal in self.animals:
            all_animals_care += animal.money_for_care
        if self.__budget >= all_animals_care:
            self.__budget -= all_animals_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        full_info = f"You have {len(self.animals)} animals\n"
        lions_info = ""
        lions_count = 0
        tigers_info = ""
        tigers_count = 0
        cheetahs_info = ""
        cheetahs_count = 0
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions_info += repr(animal) + "\n"
                lions_count += 1
            elif animal.__class__.__name__ == "Tiger":
                tigers_info += repr(animal) + "\n"
                tigers_count += 1
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs_info += repr(animal) + "\n"
                cheetahs_count += 1

        lions_info = f"----- {lions_count} Lions:\n" + lions_info
        tigers_info = f"----- {tigers_count} Tigers:\n" + tigers_info
        cheetahs_info = f"----- {cheetahs_count} Cheetahs:\n" + cheetahs_info
        full_info += lions_info + tigers_info + cheetahs_info
        return full_info[:-1]

    def workers_status(self):
        workers_full_info = f"You have {len(self.workers)} workers\n"
        keeper_info = ""
        keeper_count = 0
        caretaker_info = ""
        caretaker_count = 0
        vet_info = ""
        vet_count = 0
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keeper_info += repr(worker) + "\n"
                keeper_count += 1
            elif worker.__class__.__name__ == "Caretaker":
                caretaker_info += repr(worker) + "\n"
                caretaker_count += 1
            elif worker.__class__.__name__ == "Vet":
                vet_info += repr(worker) + "\n"
                vet_count += 1

        keeper_info = f"----- {keeper_count} Keepers:\n" + keeper_info
        caretaker_info = f"----- {caretaker_count} Caretakers:\n" + caretaker_info
        vet_info = f"----- {vet_count} Vets:\n" + vet_info
        workers_full_info += keeper_info + caretaker_info + vet_info
        return workers_full_info[:-1]


# zoo = Zoo("Zootopia", 3000, 5, 8)
# wk = Vet("John", 33, 1245)
# print(zoo.hire_worker(wk))
# print(zoo.fire_worker("John"))


# zoo = Zoo("Zootopia", 3000, 5, 8)
# ch = Cheetah("Cheeto", "Male", 2)
# li = Lion("Lili", "Female", 5)
# zoo.add_animal(ch, 50)
# zoo.add_animal(li, 45)
# print(zoo.animals_status())
