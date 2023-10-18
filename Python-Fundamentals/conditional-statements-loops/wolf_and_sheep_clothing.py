# Wolf in sheep's clothing

queue = input().split(", ")

for i in range(len(queue)):
    if queue[i] == "wolf":
        if i == len(queue) - 1:
            print(f"Please go away and stop eating my sheep")
            break
        wolf_place = len(queue) - i
        print(f"Oi! Sheep number {wolf_place - 1}! You are about to be eaten by a wolf!")
