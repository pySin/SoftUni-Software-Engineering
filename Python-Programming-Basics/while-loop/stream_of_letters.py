# Stream Of Letters
secret_command = ""
normal_word = ""
inner_word = ""

while True:

    if len(secret_command) == 3:
        # print("In 3 len")
        normal_word += inner_word + " "
        secret_command = ""
        inner_word = ""

    letter = input()

    if letter == "End":
        break

    letter_present = False

    if not letter.isalpha():
        continue

    if letter == "c":
        for i in range(len(secret_command)):
            if secret_command[i] == "c":
                letter_present = True
                break

        if letter_present:
            inner_word += letter
            continue
        else:
            secret_command += letter
            continue

    if letter == "o":
        for i in range(len(secret_command)):
            if secret_command[i] == "o":
                letter_present = True
                break

        if letter_present:
            inner_word += letter
            continue
        else:
            secret_command += letter
            continue

    if letter == "n":
        for i in range(len(secret_command)):
            if secret_command[i] == "n":
                letter_present = True
                break

        if letter_present:
            inner_word += letter
            continue
        else:
            secret_command += letter
            continue

    inner_word += letter


print(f"{normal_word}")
