# -=- Parameter changing method

import random


class MyClass:
    def __init__(self, num_1: int, num_2: int, text_1: str):
        self.num_1 = num_1
        self.num_2 = num_2
        self.text_1 = text_1

    def elongate_text_1(self, char_number: int):
        chars = "abcd"
        for i in range(char_number):
            self.text_1 += chars[random.randint(0, 3)] + chars[random.randint(0, 3)]


m = MyClass(2, 5, "Go")
m.elongate_text_1(12)
print(m.text_1)