# Next Version

version_in_numbers = list(map(int, input().split(".")))

if version_in_numbers[2] == 9:
    version_in_numbers[2] = 0
    version_in_numbers[1] += 1
else:
    version_in_numbers[2] += 1

if version_in_numbers[1] > 9:
    version_in_numbers[1] = 0
    version_in_numbers[0] += 1


# print(f"{version_in_numbers[0]}.{version_in_numbers[1]}.{version_in_numbers[2]}")
print(".".join(map(str, version_in_numbers)))
