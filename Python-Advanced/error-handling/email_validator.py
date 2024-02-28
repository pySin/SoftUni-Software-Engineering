# Email Validator


class NameTooShort(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass




def call_functions():
    email_min_length = 4
    valid_domains = [".com", ".bg", ".org", ".net"]
    email = input()
    while email != "End":
        email_name = email.split("@")[0]
        email_domain = email.split(".")[-1]
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")
        elif len(email_name) <= email_min_length:
            raise NameTooShort("Name must be more than 4 characters")
        elif "." + email_domain not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        else:
            print("Email is valid")
        email = input()


if __name__ == "__main__":
    call_functions()


# class NameTooShortError(Exception):
#     pass
#
#
# class MustContainAtSymbolError(Exception):
#     pass
#
#
# class InvalidDomainError(Exception):
#     pass
#
#
# def email_too_short():
#     raise NameTooShortError("Name must be more than 4 characters")
#
#
# def not_at_symbol():
#     raise MustContainAtSymbolError("Email must contain @")
#
#
# def invalid_domain():
#     raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
#
#
# def call_functions():
#     email_min_length = 4
#     valid_domains = [".com", ".bg", ".org", ".net"]
#     email = input()
#     while email != "End":
#         email_name = email.split("@")[0]
#         email_domain = email.split(".")[-1]
#         if "@" not in email:
#             not_at_symbol()
#         elif len(email_name) <= email_min_length:
#             email_too_short()
#         elif "." + email_domain not in valid_domains:
#             invalid_domain()
#         else:
#             print("Email is valid")
#         email = input()
#
#
# if __name__ == "__main__":
#     call_functions()
