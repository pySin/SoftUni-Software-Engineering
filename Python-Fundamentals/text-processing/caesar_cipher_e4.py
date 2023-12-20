# Caesar Cipher


def ascii_values(sentence):
    values = [ord(x) for x in sentence]
    return values


def cipher(sentence):
    values = ascii_values(sentence)
    cipher_values = [chr(x + 3) for x in values]
    return cipher_values


if __name__ == "__main__":
    main_sentence = input()
    cipher_list = cipher(main_sentence)
    print(f"{''.join(cipher_list)}")
