# Countdown Iterator


class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.end:
            raise StopIteration()
        current_count = self.count
        self.count -= 1
        return current_count


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
print("\n++++++++==++++++++++++")
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
