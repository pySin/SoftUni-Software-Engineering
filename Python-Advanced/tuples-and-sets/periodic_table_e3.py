# Periodic Table


n = int(input())
unique_elements = set()

for _ in range(n):
    current_elements = {x for x in input().split()}
    unique_elements = unique_elements | current_elements

# print(*unique_elements, sep="\n")
# print(*unique_elements, sep=" - ")
print(*unique_elements)
