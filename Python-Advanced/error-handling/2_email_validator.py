class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


EMAIL_MIN_LENGTH = 5
VALID_DOMAINS = {'.com', '.bg', '.org', '.net'}

email = input()
while email != "End":
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if len(email.split('@')[0]) < EMAIL_MIN_LENGTH:
        raise MustContainAtSymbolError("Name must be more than 4 characters")
    domain = '.' + email.split('.')[-1]
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    email = input()
