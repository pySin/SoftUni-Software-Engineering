# Josephus Permutation


people = [int(person) for person in input().split()]
steps = int(input())

josephus_permutation = []
people_index = 0
while people:
    for step in range(steps):
        if people_index == len(people):
            people_index = 0
        people_index += 1
    josephus_permutation.append(people.pop(people_index - 1))
    people_index -= 1

[print(step, end="") for step in str(josephus_permutation) if step != " "]
