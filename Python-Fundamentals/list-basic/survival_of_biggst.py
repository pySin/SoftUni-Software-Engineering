# Survival of the biggest


integers = list(map(int, input().split()))
numbers_to_remove = int(input())

for i in range(numbers_to_remove):
    smallest_number_index = integers.index(min(integers))
    integers.pop(smallest_number_index)

print(", ".join(map(str, integers)))
