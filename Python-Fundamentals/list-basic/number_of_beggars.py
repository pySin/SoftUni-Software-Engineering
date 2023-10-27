# Number of beggars

beggar_turns = input().split(", ")
beggar_turns = [int(number) for number in beggar_turns]
count_of_beggars = int(input())


beggars_income = [0 for one_beggar in range(count_of_beggars)]
# print(beggars_income)

turn = 0
# print(beggar_turns[turn])
while turn < len(beggar_turns):
    for beggar in range(count_of_beggars):
        beggars_income[beggar] += beggar_turns[turn]
        turn += 1
        if turn == len(beggar_turns):
            break

print(beggars_income)
