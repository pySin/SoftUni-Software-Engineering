# Barcode Generator

# Две четирицифрени числа, които показват обхвата на баркодовете, които трябва да промените.
# Първи ред – четирицифрено число – началото на обхвата. Цяло число в интервала [1000…9999]
# Втори ред – четирицифрено число – края на обхвата. Цяло число в интервала [1000…9999]

low_number = input()
high_number = input()


odd_numbers = ""

for i in range(4):
    current_low_number = low_number[i]
    current_high_number = high_number[i]

    for range_number in range(int(current_low_number), int(current_high_number) + 1):
        if range_number % 2 != 0:
            odd_numbers += str(range_number)
    odd_numbers += "$"

first_numbers = ""
second_numbers = ""
third_numbers = ""
forth_numbers = ""

x = 1
for number in range(len(odd_numbers)):
    if odd_numbers[number] == "$":
        x += 1
        continue

    if x == 1:
        first_numbers += str(odd_numbers[number])
    elif x == 2:
        second_numbers += str(odd_numbers[number])
    elif x == 3:
        third_numbers += str(odd_numbers[number])
    elif x == 4:
        forth_numbers += str(odd_numbers[number])

for a in range(len(first_numbers)):
    for b in range(len(second_numbers)):
        for c in range(len(third_numbers)):
            for d in range(len(forth_numbers)):
                print(first_numbers[a]+second_numbers[b]
                      + third_numbers[c]+forth_numbers[d], end=" ")
