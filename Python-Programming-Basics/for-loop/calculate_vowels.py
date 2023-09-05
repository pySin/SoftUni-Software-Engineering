# calculate vowels

my_text = input()
vowels_calculation = 0

for i in range(1, len(my_text), 1):
    if my_text[i] == "a":
        vowels_calculation += 1
    if my_text[i] == "e":
        vowels_calculation += 2
    if my_text[i] == "i":
        vowels_calculation += 3
    if my_text[i] == "o":
        vowels_calculation += 4
    if my_text[i] == "u":
        vowels_calculation += 5

print(vowels_calculation)
