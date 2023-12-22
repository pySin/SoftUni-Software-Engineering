# Digits, letters and other


single_string = input()

digits = ""
letters = ""
other = ""

for i in range(len(single_string)):
    if single_string[i].isalpha():
        letters += single_string[i]
    elif single_string[i].isdigit():
        digits += single_string[i]
    else:
        other += single_string[i]

print(digits)
print(letters)
print(other)
