# Encrypting Password
import re


def check_password(password: str):
    pattern = r"((.+?)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\2)"
    result = re.findall(pattern, password)
    # print(result)
    if result:
        print(f"Password: {result[0][2]}{result[0][3]}{result[0][4]}{result[0][5]}")
    else:
        print("Try another password!")


def call_functions():
    n = int(input())

    for line in range(n):
        password = input()
        check_password(password)


if __name__ == "__main__":
    call_functions()
