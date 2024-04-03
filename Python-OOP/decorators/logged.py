# Logged


def logged(func):
    def wrapper(*args, **kwargs):
        expression = f"you called {func.__name__}{args}\nit returned {func(*args)}"
        return expression
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
