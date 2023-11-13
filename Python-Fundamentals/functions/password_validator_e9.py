# Password Validator

def check_password(pss):
    phrases = []
    if not 6 <= len(pss) <= 10:
        phrases.append("Password must be between 6 and 10 characters")

    if not pss.isalnum():
        phrases.append("Password must consist only of letters and digits")

    digits = 0
    for letter in pss:
        if letter.isnumeric():
            digits += 1

    if digits < 2:
        phrases.append("Password must have at least 2 digits")

    if not phrases:
        phrases.append("Password is valid")

    return phrases


password = input()
results = check_password(password)
for print_line in results:
    print(print_line)
