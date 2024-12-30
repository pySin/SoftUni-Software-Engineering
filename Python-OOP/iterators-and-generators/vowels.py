# Vowels


class vowels:

    def __init__(self, chars: str):
        self.chars = chars
        self.start = -1
        self.end = len(chars) - 1
        self.vowels = "AEIOUYaeiouy"

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration()
        self.start += 1
        if self.chars[self.start] in self.vowels:
            return self.chars[self.start]
        return self.__next__()


v = vowels('Abcedifuty0o')
for vowel in v:
    print(vowel)
