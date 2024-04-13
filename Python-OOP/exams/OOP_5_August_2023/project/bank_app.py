from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: list = []
        self.clients: list = []

    def add_loan(self, loan_type: str):
        valid_types_loans = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
        if loan_type not in valid_types_loans:
            raise Exception("Invalid loan type!")

        self.loans.append(valid_types_loans[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        valid_client_types = {"Student": Student, "Adult": Adult}
        if client_type not in valid_client_types:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        self.clients.append(valid_client_types[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client_loans = {"Student": "StudentLoan", "Adult": "MortgageLoan"}
        client = next((c for c in self.clients if c.client_id == client_id), None)

        if client_loans[client.__class__.__name__] != loan_type:
            raise Exception("Inappropriate loan type!")

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                client.loans.append(loan)
                self.loans.remove(loan)
                return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if not client:
            raise Exception("No such client!")

        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                changed_loans += 1
                loan.increase_interest_rate()
        return f"Successfully changed {changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_interests = 0
        for client in self.clients:
            if client.interest < min_rate:
                changed_interests += 1
                client.increase_clients_interest()
        return f"Number of clients affected: {changed_interests}."

    def get_statistics(self):
        active_clients = f"Active Clients: {len(self.clients)}"
        total_income = f"Total Income: {sum([c.income for c in self.clients]):.2f}"
        granted_loans = f"Granted Loans: {sum([len(l.loans) for l in self.clients])}, " \
                        f"Total Sum: {sum([sum([pl.amount for pl in l.loans]) for l in self.clients]):.2f}"
        available_loans = f"Available Loans: {len(self.loans)}, Total Sum: {sum([al.AMOUNT for al in self.loans]):.2f}"
        average_interest = sum([cl.interest for cl in self.clients]) / len(self.clients) if len(self.clients) > 0 else 0
        avg_client_interest = f"Average Client Interest Rate: {average_interest:.2f}"

        statistics = "\n".join([active_clients, total_income, granted_loans, available_loans, avg_client_interest])
        return statistics
