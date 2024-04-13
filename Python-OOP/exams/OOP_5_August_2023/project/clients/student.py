from project.clients.base_client import BaseClient


class Student(BaseClient):
    INTEREST_RATE = 2.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.INTEREST_RATE)

    def increase_clients_interest(self):
        self.interest += 1
