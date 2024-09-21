# Sequence Repeat


class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.number:
            current_alpha = self.sequence[self.current % len(self.sequence)]
            self.current += 1
            return current_alpha
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print("\n+=============+")
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')