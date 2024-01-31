# Supermarket
from collections import deque

command = input()
supermarket_queue = deque([])

while command != "End":

    if command == "Paid":
        for i in range(len(supermarket_queue)):
            print(supermarket_queue.popleft())
    else:
        supermarket_queue.append(command)

    command = input()

print(f"{len(supermarket_queue)} people remaining.")
