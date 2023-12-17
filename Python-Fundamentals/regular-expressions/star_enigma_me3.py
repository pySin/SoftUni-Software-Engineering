# Star Enigma
import re


def decrypt_message(message):
    pattern = r"[s, t, a, r]"
    key_factor = len(re.findall(pattern, message, re.IGNORECASE))
    new_message = [chr(ord(letter) - key_factor) for letter in message]
    return "".join(new_message)


def extract_data(message):
    # pattern = r"@([A-Za-z]+).*:([0-9]+).*!([A, D])!.*->([0-9]+)"
    pattern = r"@([A-Za-z]+)[^@\-!:>]*:([0-9]+)[^@\-!:>]*!([A, D])![^@\-!:>]*->([0-9]+)"
    result = re.findall(pattern, message)
    if result:
        return result
    else:
        return None


def call_functions():
    number_of_messages = int(input())

    attacks = [0, []]
    destroy = [0, []]

    for message in range(number_of_messages):
        command = input()
        decrypted_message = decrypt_message(command)
        # print(decrypted_message)
        war_data = extract_data(decrypted_message)
        # print(f"War data: {war_data}")
        if war_data:
            if war_data[0][2] == "A":
                attacks[0] += 1
                attacks[1].append(war_data[0][0])

            elif war_data[0][2] == "D":
                destroy[0] += 1
                destroy[1].append(war_data[0][0])
    print(f"Attacked planets: {attacks[0]}")
    if attacks[0] > 0:
        for planet in sorted(attacks[1]):
            print(f"-> {planet}")
    print(f"Destroyed planets: {destroy[0]}")
    if destroy[0] > 0:
        for planet in sorted(destroy[1]):
            print(f"-> {planet}")


if __name__ == "__main__":
    call_functions()
