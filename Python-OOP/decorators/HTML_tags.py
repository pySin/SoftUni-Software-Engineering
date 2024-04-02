# HTML tags


def tags(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator


# @tags('h1')
# def to_upper(text):
#     return text.upper()
#
#
# print(to_upper('hello'))


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
