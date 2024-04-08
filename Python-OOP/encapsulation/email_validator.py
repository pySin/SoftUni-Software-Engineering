# Email Validator


class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        # print(self.min_length, len(name))
        if self.min_length > len(name):
            return False
        return True

    def __is_mail_valid(self, mail):

        # print("Mail: " + mail, mails)
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain):
        # print(domain, domains)
        if domain in self.domains:
            return True
        return False

    def validate(self, email):
        name = email[:email.index("@")]
        mail = email[email.index("@") + 1:][:email[email.index("@") + 1:].index(".")]
        domain = email[email.index("@") + 1:][email[email.index("@") + 1:].index(".") + 1:]
        if all([self.__is_name_valid(name), self.__is_mail_valid(mail), self.__is_domain_valid(domain)]):
            return True
        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
