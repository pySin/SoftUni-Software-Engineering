# Profile


class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, user):
        if not 5 <= len(user) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = user

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, pass_w):
        if not len(pass_w) > 7 or not any([letter.isupper() for letter in pass_w]) \
                or not any([letter.isdigit() for letter in pass_w]):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = pass_w

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
