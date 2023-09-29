# Multiply Table

# Входът е цяло трицифрено число в интервала [111…999].

reverse_number = int(input())
reverse_number_string = str(reverse_number)

for i in range(1, int(reverse_number_string[2]) + 1):
    for j in range(1, int(reverse_number_string[1]) + 1):
        for h in range(1, int(reverse_number_string[0]) + 1):
            print(f"{i} * {j} * {h} = {i * j * h};")
