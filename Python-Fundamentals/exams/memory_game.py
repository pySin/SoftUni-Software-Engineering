# Memory game


number_elements = input().split()

command = input()
number_of_moves = 0

while command != "end":

    number_of_moves += 1

    index_1, index_2 = list(map(int, command.split()))

    if index_1 == index_2 or index_1 not in range(len(number_elements)) \
            or index_2 not in range(len(number_elements)):
        number_elements = number_elements[:len(number_elements) // 2] \
                          + [f"-{number_of_moves}a"] * 2 + number_elements[len(number_elements) // 2:]
        print("Invalid input! Adding additional elements to the board")
        command = input()
        continue

    if number_elements[index_1] == number_elements[index_2]:
        print(f"Congrats! You have found matching elements - {number_elements[index_1]}!")
        if index_2 > index_1:
            number_elements.pop(index_2)
            number_elements.pop(index_1)
        else:
            number_elements.pop(index_1)
            number_elements.pop(index_2)

    else:
        print("Try again!")

    if not number_elements:
        print(f"You have won in {number_of_moves} turns!")
        break

    command = input()

if number_elements:
    print("Sorry you lose :(")
    print(" ".join(number_elements))
