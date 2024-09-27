# Tale Skip


class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0
        self.end = count

    def __iter__(self):
        return self

    def __next__(self):
        current_step = self.start
        if self.start == self.end:
            raise StopIteration()
        self.start += 1
        return current_step * self.step


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
