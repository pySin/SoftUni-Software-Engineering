# Stack of Strings


class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            raise ValueError("Element is not a string, please add only strings")
        self.data.append(element)

    def pop(self):
        popped = self.data.pop()
        return popped

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        reversed_data = list(reversed(self.data))
        return f'[{", ".join(reversed_data)}]'


s = Stack()
s.push("one")
s.push("two")
print(s)
