# Decipher this


cipher_message = input().split()


final_message = ""
for word in cipher_message:

    word_list = list(word)
    first_number = [x for x in word_list if x.isdigit()]
    following_letters = [letter for letter in word_list if not letter.isdigit()]
    # word_list[1], word_list[-1] = word_list[-1], word_list[1]
    first_letter = chr(int("".join(first_number)))
    print(first_letter)
    print(following_letters)
    following_letters[0], following_letters[-1] = following_letters[-1], following_letters[0]
    print(following_letters)
    current_word = "".join(list(first_letter) + following_letters)
    print(current_word)
    final_message += current_word + " "

print(final_message[:-1])
