# No Vowels

normal_text = input()

consonant_text = [letter for letter in normal_text if letter.lower() not in "aouei"]
print("".join(consonant_text))
