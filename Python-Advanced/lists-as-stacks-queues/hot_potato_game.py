# Hot Potato Game
from collections import deque

kids_names = deque(input().split(" "))
number_of_tosses = int(input())


while True:
    if len(kids_names) == 1:
        print(f"Last is {kids_names[0]}")
        break

    for i in range(number_of_tosses):
        kids_names.append(kids_names.popleft())
    print(f"Removed {kids_names.pop()}")
