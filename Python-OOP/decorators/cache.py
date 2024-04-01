# Cache

def cache(func):
    def wrapper(n):
        if not wrapper.log.get(n):
            wrapper.log[n] = func(n)
        return wrapper.log[n]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


fibonacci(4)
print(fibonacci.log)












# --

# from functools import wraps
#
# def cache(func):
#     log_x = {}
#     # n_nums = []
#
#     # @wraps(func)
#     def wrapper(n):
#         # n_nums.append(n)
#         result = func(n)
#         log_x[n] = result
#         # print(log)
#         # if n == max(n_nums):
#         #     log = log_x
#         log = log_x
#         return result
#     return wrapper
#
#
# @cache
# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# fibonacci(4)
# print(fibonacci.log)
