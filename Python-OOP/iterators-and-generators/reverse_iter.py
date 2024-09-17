# Reverse iter


class reverse_iter:
    def __init__(self, collection: list):
        self.collection = collection
        self.reverse_start = len(collection)
        self.reverse_end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.reverse_start == self.reverse_end:
            raise StopIteration()
        self.reverse_start -= 1
        return self.collection[self.reverse_start]


rv = reverse_iter([1, 2, 3, 4])

for it in rv:
    print(it)

