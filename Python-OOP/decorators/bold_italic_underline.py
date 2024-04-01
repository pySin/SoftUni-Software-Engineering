# Bold, Italic, Underline


def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        return f"<b>{result}</b>"
    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        return f"<i>{result}</i>"
    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        return f"<u>{result}</u>"
    return wrapper


@make_bold  # third wrapping
@make_italic  # second wrapping
@make_underline  # first wrapping
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))


# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f"Hello, {name}"
#
#
# print(greet("Peter"))
