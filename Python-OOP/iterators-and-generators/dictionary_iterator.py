# Dictionsry Iterator


class dictionary_iter:
    def __init__(self, dict_o: dict):
        self.dict_o = list(dict_o.items())
        self.start = 0
        self.end = len(self.dict_o)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.start < self.end:
            raise StopIteration()
        else:
            current_pair = self.dict_o[self.start]
            self.start += 1
            return current_pair


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
