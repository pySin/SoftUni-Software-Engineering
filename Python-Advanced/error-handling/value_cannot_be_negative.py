# Value Can Not Be Negative

class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative  # Brackets if we want to give a message.
