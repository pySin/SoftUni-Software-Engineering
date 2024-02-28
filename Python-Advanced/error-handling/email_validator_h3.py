import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidNameError(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")

pattern_name_to_short = r"[a-zA-Z]{5,}"
pattern_at = r'[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]{2,}'
pattern_valid_name = r"[a-zA-Z0-9_]+$"

email = input("Enter an email address: ")

while email != "End":

    name = email.split('@')[0]
    if len(name) <= 4:
        raise NameTooShortError("Name in the email is too short")

    print("Email is valid")

    if not re.search("@", email):
        raise MustContainAtSymbolError("Email must contain @")

    domain = email.split(".")[-1]
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")

    if not re.match(pattern_valid_name, name):
        raise InvalidNameError("Name can contain only: letters, digits and underscores")
    email = input()