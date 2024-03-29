# Smartphone


class Smartphone:
    """Defines smartphone product!"""
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        """Turns On or Of a smartphone."""
        self.is_on = True if self.is_on is False else False

    def install(self, app, app_memory):
        if self.memory >= app_memory:
            if self.is_on:
                self.memory -= app_memory
                self.apps.append(app)
                return f"Installing {app}"
            else:
                return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
print(smartphone.__doc__)
print(smartphone.power.__doc__)
print(smartphone.__dict__)
print(Smartphone.__dict__)
