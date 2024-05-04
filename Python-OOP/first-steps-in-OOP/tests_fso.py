# First Steps in OOP
from typing import List, Optional, Union

# class Car:
#     def __init__(self, model):
#         self.model = model
#
#     def drive(self):
#         print(f"Drive: {self.model}")
#
#
# ford = Car("Ford Focus RS")
# print(ford.model)
# ford.drive()
# nissan = Car("Nissan GTR")
# toyota = Car("Toyota GR86")
# print(toyota.__dict__)
#
# # Call Object function through the class
#
# print(Car.drive(ford))

# --

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def has_birthday(self):
#         self.age += 1
#
#
# ivan = Person("Ivan", 30)
# print(ivan.age)
# ivan.has_birthday()
# print(ivan.age)

# -- Annotation train (Optional)


# annotated_variable: List[Union[int, str]] = []
#
# letters = "abcderghilk"
#
# for i in range(8):
#     annotated_variable.append(i)
#     annotated_variable.append(letters[i])
#
# print(annotated_variable)
