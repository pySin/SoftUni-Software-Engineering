# Account
from typing import Optional


class Account:
    def __init__(self, owner: str, amount: Optional[int] = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: list = []
        self.balance = None

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def get_transactions(self):
        return self._transactions

    def below_zero_check(self, amount):
        if (self.amount + sum(self._transactions)) + amount < 0:
            raise ValueError("sorry cannot go in debt")

    def handle_transaction(self, transaction_amount):
        self.below_zero_check(transaction_amount)
        # self.amount += transaction_amount
        self._transactions.append(transaction_amount)
        return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if type(amount) != int:
            raise ValueError("please use int for amount")
        self.below_zero_check(amount)
        self._transactions.append(amount)
        return f"New balance: {self.amount}"

    # def balance(self):
    #     return self.amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        account_x = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        account_x._transactions = self._transactions + other.get_transactions()
        return account_x


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
