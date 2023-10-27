# Multiples List

factor = int(input())
count = int(input())

multiplied_list = []

for i in range(1, count + 1):
    multiplied_list.append((factor * i))

print(multiplied_list)
