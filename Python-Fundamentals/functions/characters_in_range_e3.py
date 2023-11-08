# Characters in range

def characters_range(first_character, second_character):
    first_ascii_number = ord(first_character)
    second_ascii_number = ord(second_character)
    chr_range = [chr(char) for char in range(first_ascii_number + 1, second_ascii_number)]
    return " ".join(chr_range)


character_one = input()
character_two = input()

print(characters_range(character_one, character_two))
