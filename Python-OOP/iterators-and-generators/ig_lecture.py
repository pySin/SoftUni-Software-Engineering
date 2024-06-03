# class Person:
#     def __init__(self, age):
#         self.name = "asd"
#         self._asd = 12
#         self.__age = age
#
#
# p = Person(44)
#
# for item in p:
#     print(item)

# -- filter returns generator which depletes after one iteration
# iterators deplete as well.

# result = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
#
# for _ in result:
#     print(_)
#
# for _ in result:  # after the 1st iteration the sequence is over and the second loop
#     print(_)      # has nothing to iterate over.

# ----

# class Person:
#     def __init__(self, age):
#         self.name = "asd"
#         self._asd = 12
#         self.__age = age
#
#
# p = Person(44)
#
# for item in p:
#     print(item)

# -- Iterator from an iterable

# my_list = [4, 7, 0, 3]
# # get an iterator using iter()
# my_iter = iter(my_list)
# print(next(my_iter))  # 4
# print(next(my_iter))  # 7
# print(my_iter.__next__())  # 0
# print(my_iter.__next__())  # 3
# next(my_iter)

# my_list = [1, 2, 3, 4]
# my_iter_list = iter(my_list)
# print(my_iter_list)
# print(next(my_iter_list))
# print(next(my_iter_list))
# print(next(my_iter_list))
# print(next(my_iter_list))
# print(next(my_iter_list))

# -- FOR loop under the hood is a WHILE loop
# my_list = [1, 2, 3, 4]
# my_iter_list = iter(my_list)

# while True:  # Creation of a for loop
#     try:
#         print(next(my_iter_list))
#     except StopIteration:
#         pass

# --

# my_list = [1, 2, 3, 4]
# my_iter_list = iter(my_list)
# print(my_iter_list.__next__())

# -- Make class Person iterable / iterators

# class Person:
#     def __init__(self, age, name):
#         self.name = name
#         self._asd = 12
#         self.__age = age
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == len(self.name) - 1:
#             self.index = -1  # Allow the iteration to start again.
#             raise StopIteration()
#         self.index += 1
#         return self.name[self.index]
#
#
# p = Person(44, "Vermont")
#
# for letter in p:
#     print(letter)
#
# for letter in p:
#     print(letter)

# --- Generators

# def first_n(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
#
# caller = first_n(5)
# print(next(caller))
# print(next(caller))

# --

# def my_gen():
#     n = 1
#     print('This is printed first')
#     yield n  # after this yield the function stops
#     n += 1
#     print('This is printed second')
#     yield n  # Continue from the second yield
#     n += 1
#
#     print('This is printed at last')
#     yield n
#
#
# gen = my_gen()
# print(next(gen))
# print(next(gen))

# --
# def first_n(n):
#     num = 0
#     for i in range(1, n + 1):
#         yield i ** 2
#
#
# gen = first_n(12)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# -- Generator expression

# my_list = [1, 3, 6, 10]
#
# gen_1 = ((x**2 for x in my_list))
#
# print(gen_1.__class__.__name__)
# print(type(gen_1))

# --

# import time


# def gen_1():
#     x = 1
#     while True:
#         yield x
#         x += 1
#         time.sleep(2)
#
#
# for value in gen_1():
#     print(value)

# def run_gen(times, gen_func):  # Called function and uncalled function!!!
#     nums = []
#     for ni in range(times):
#         nums.append(next(gen_func))  # If we call  the function here it starts from the beginning every time
#     return nums                      # and makes "x" 1. Continue from the STOPPED place!
#
#
# print(run_gen(5, gen_1()))  # The function must be called here

# -- Endless Generator

# def gen():
#
#     while True:
#         yield 1
#
#
# print(gen().__next__())
# print(next(gen()))
# x = 0
# for i in gen():
#     if x == 5:
#         break
#     print(i)
#     x += 1

# --

# class IterThing:
#     collection = [1, 2, 3, 4]
#     n = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n == len(self.collection) - 1:
#             raise StopIteration
#         self.n += 1
#         return self.collection[self.n]
#
#
# it = IterThing()
# for num in it:
#     print(num)

# -- Basic Generator

# def gen1():
#     x = 1
#     while True:
#         yield x
#         x += 1
#
#
# called_gen1 = gen1()
# print(next(called_gen1))
# print(next(called_gen1))
# print(next(called_gen1))
# print(next(called_gen1))
