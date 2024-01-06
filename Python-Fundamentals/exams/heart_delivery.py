# Heart Delivery


even_integers = [int(x) for x in input().split("@")]

command = input()


jump_index = 0
while command != "Love!":

    instructions = command.split()

    if instructions[0] == "Jump":
        jump_index += int(instructions[1])
        if jump_index >= len(even_integers):
            jump_index = 0

        if even_integers[jump_index] == 0:
            print(f"Place {jump_index} already had Valentine's day.")
        else:
            even_integers[jump_index] -= 2
            if even_integers[jump_index] == 0:
                print(f"Place {jump_index} has Valentine's day.")

    command = input()


even_integers = [x for x in even_integers if x > 0]


print(f"Cupid's last position was {jump_index}.")
if sum(even_integers) == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(even_integers)} places.")
