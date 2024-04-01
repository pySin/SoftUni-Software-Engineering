# Decorators


# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi
#
#
# hello = hello_function()
# print(hello())

# -- Enclosure in Decorators


# def print_message(message):
#     def message_sender():  # Has access to "message" variable
#         "Nested Function"
#         print(message)
#     message_sender()
#
#
# print_message("Some random message")

# -- Decorator Wrap


# def uppercase(function):
#     def wrapper():
#         result = function()
#         uppercase_result = result.upper()
#         return uppercase_result
#
#     return wrapper
#
#
# @uppercase
# def say_hi():
#     return "hello there"
#
#
# print(say_hi())
# print(uppercase(say_hi()))

# --
# from functools import wraps
#
#
# def uppercase(function):
#     @wraps(function)  # -- Transfers the source function data to the Decorator.
#     def wrapper():
#         "From Wrapper"
#         result = function()
#         uppercase_result = result.upper()
#         return uppercase_result
#
#     return wrapper
#
#
# @uppercase
# def say_hi():
#     """Saying Hi"""
#     return "hello there"


# -- Passing Data to the decorator itself

# def uppercase(n_letters=2):  # Default value option
#     def decorator(function):
#         def wrapper():
#             "From Wrapper"
#             result = function()
#             uppercase_result = result[:n_letters].upper()
#             lowercase_result = result[n_letters:].lower()
#
#             return uppercase_result + lowercase_result
#
#         return wrapper
#     return decorator
#
#
# @uppercase()  # Can use optional empty brackets only have set an optional value.
# def say_hi():
#     """Saying Hi"""
#     return "hello there"


# print(say_hi())

# -- same with args

# -- Passing arguments to the Decorator and passing a function to the Wrapper

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @repeat(4)
# def say_hi():
#     print("Hello")
#
#
# say_hi()

# --

# def repeat(n):
#     def decorator(function):
#         def wrapper(*args, **kwargs):  # This will work for any types of arguments passed to the function.
#             result = function(*args, **kwargs)
#             return result * n
#         return wrapper
#     return decorator
#
#
# @repeat(4)
# def say(word):
#     return word
#
#
# print(say("Hello"))

# -- Classes as Decorators

# class Fibonacci:
#     def __init__(self):
#         self.cache = {}
#
#     def __call__(self, n):
#         if n not in self.cache:
#             if n == 0:
#                 self.cache[0] = 0
#             elif n == 1:
#                 self.cache[1] = 1
#             else:
#                 self.cache[n] = self(n-1) + self(n-2)
#
#         return self.cache[n]
#
#
# fib = Fibonacci()
# for i in range(5):
#     print(fib(i))
#     print(fib.cache)

# --


# class func_logger:
#     _logfile = 'out.log'
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args):
#         log_string = self.func.__name__ + " was called"
#         with open(self._logfile, 'a') as opened_file:
#             opened_file.write(log_string + '\n')
#         return self.func(*args)
#
#
# @func_logger
# def say_hi(name):
#     print(f"Hi, {name}")
#
#
# @func_logger
# def say_bye(name):
#     print(f"Bye, {name}")
#
#
# say_hi("Peter")
# say_bye("Peter")

# --

# nums = [12, 4, 6, 8]
# nums_2 = [1, 6, "Hose"]
#
# if all(isinstance(el, int) and el % 2 == 0 for el in nums_2):
#     print("All elements are even numbers!")
# else:
#     print("There is an element that's not even number")

# --


# def b1():
#     def __x__():
#         return 1
#
#
# print(b1.x)


# class First:
#     print("In Class")
#
#     def __call__(self, *args, **kwargs):
#         print("First Call")
#         return "Return First Class"
#
#
# first = First()
# first()  # The Object is callable.

# --

# text = "   "
# if text.strip():
#     print("Zero text")
# else:
#     print("Empty String is False")

# print(2 ** 7)

# --

# result = all([1 < 2, 3 == 3, 4 > 1])
# print(result)

# @property direct call

# class PCall:
#
#     @property
#     def give_info(self):
#         return "info given"
#
#     def internal_info_call(self):
#         print(self.give_info)
#
#
# pc = PCall()
# print(pc.give_info)
# pc.internal_info_call()

# -- Decorator keep target function metadata

# from functools import wraps
#
#
# def modify(func):
#     # @wraps(func)
#     def wrapper():
#         result = func()
#         return result + "Modified"
#     return wrapper
#
#
# @modify
# def sample_function():
#     return "Target Function"
#
#
# print(sample_function.__name__)
