# Three Letter Combinations

# ⦁	Малка буква от английската азбука за начало на интервала – от ‘a’ до ‚z’.
# ⦁	Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
# ⦁	Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.

first_range_letter = input()
last_range_letter = input()
middle_range_letter = input()

count_combinations = 0

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabet)):
    if alphabet[i] == first_range_letter:
        for j in range(len(alphabet)):
            if alphabet[j] == last_range_letter:
                for h in range(i, j + 1):
                    for a in range(i, j + 1):
                        for b in range(i, j + 1):
                            if alphabet[h] != middle_range_letter and alphabet[a] != middle_range_letter\
                                    and alphabet[b] != middle_range_letter:
                                count_combinations += 1
                                print(alphabet[h] + alphabet[a] + alphabet[b], end=" ")
print(count_combinations)
