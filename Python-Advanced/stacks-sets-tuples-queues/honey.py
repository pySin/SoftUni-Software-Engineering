# Honey
from collections import deque


def make_honey(bees: deque, nectar: list, symbols: deque, nectar_collected: int):
    bee = bees.popleft()
    current_nectar = nectar.pop()
    symbol = symbols.popleft()
    if symbol == "+":
        nectar_collected += bee + current_nectar
    elif symbol == "-":
        nectar_collected += abs(bee - current_nectar)
    elif symbol == "*":
        nectar_collected += abs(bee * current_nectar)
    elif symbol == "/":
        if current_nectar == 0:
            return bees, nectar, symbols, nectar_collected
        nectar_collected += abs(bee / current_nectar)
    return bees, nectar, symbols, nectar_collected


def display_honey(bees: deque, nectar: list, nectar_collected: int):
    print(f"Total honey made: {nectar_collected}")
    if bees:
        print(f"Bees left: {', '.join(map(str, bees))}")

    if nectar:
        print(f"Nectar left: {', '.join(map(str, nectar))}")


def call_functions():
    bees = deque([int(x) for x in input().split()])
    nectar = [int(x) for x in input().split()]
    symbols = deque(input().split())

    nectar_collected = 0
    while bees and nectar:
        if bees[0] <= nectar[-1]:
            bees, nectar, symbols, nectar_collected = make_honey(bees, nectar, symbols, nectar_collected)
        else:
            nectar.pop()

    display_honey(bees, nectar, nectar_collected)


if __name__ == "__main__":
    call_functions()
