# Store Results


class store_results:
    information_file = "results.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open(self.information_file, "a") as f:
            f.write(f"Function {self.func.__name__} was called. Result: {self.func(*args)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
