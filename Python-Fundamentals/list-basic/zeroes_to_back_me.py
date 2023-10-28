# Zeroes To Back

integers = input().split(", ")
integers = [int(number) for number in integers]

for i in range(len(integers) - 1, - 1, - 1):
    if integers[i] == 0:
        integers.append(integers.pop(i))

print(integers)
