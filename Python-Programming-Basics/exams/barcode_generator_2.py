low_number = input()
high_number = input()

first_numbers = ""
second_numbers = ""
third_numbers = ""
forth_numbers = ""

counting = 1
for i in range(4):
    current_low_number = low_number[i]
    current_high_number = high_number[i]

    for odds in range(int(current_low_number), int(current_high_number) + 1):
        if odds % 2 != 0:
            if counting == 1:
                first_numbers += str(odds)
            if counting == 2:
                second_numbers += str(odds)
            if counting == 3:
                third_numbers += str(odds)
            if counting == 4:
                forth_numbers += str(odds)

    counting += 1

for a in range(len(first_numbers)):
    for b in range(len(second_numbers)):
        for c in range(len(third_numbers)):
            for d in range(len(forth_numbers)):
                print(first_numbers[a] + second_numbers[b] + third_numbers[c] + forth_numbers[d], end=" ")
