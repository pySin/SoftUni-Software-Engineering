# class Car:
#     capacity = 10
#
#     def __init__(self, engine):
#         self.engine = engine
#
#     def start_engine(self):
#         return "Engine started"
#
#
# car1 = Car(1)
# car2 = Car(2)
# print(id(car1))
# print(id(car2))
# print(car1.capacity)
# print(car2.capacity)
# print(car1.engine)
# print(car2.engine)
# car1.engine = 11
# print(car1.engine)
# print(car2.engine)
# car1.capacity = 16
# print(car1.capacity)
# print(car2.capacity)


# --
# class Vehicle:
#     def __init__(self, *args):
#         self.mileage = args[0]
#         self.max_speed = args[1]
#         self.gadgets = []
#
#
# car = Vehicle(100, 35)
# print(car.max_speed)
# print(car.mileage)

# -- Attributes

# class Vehicle:
#     def __init__(self, mileage, max_speed = 150):
#         self.mileage = mileage
#         self.max_speed = max_speed
#         self.gadgets = []
#
#     def __add__(self, other):
#         return "somehow we sum 2 vehicles"
#
#     def print_data(self):
#         return f"Max speed is {self.max_speed}"
#
#
# car = Vehicle(100, 35)
# car2 = Vehicle(1, 2)
#
# print(car + car2)
# print(car.__add__(car2))

# --

# class Vehicle:
#     def __init__(self, mileage, max_speed = 150):
#         self.mileage = mileage
#         self.max_speed = max_speed
#         self.gadgets = []
#         self.is_running = False
#
#     def __add__(self, other):
#         return "somehow we sum 2 vehicles"
#
#     def print_data(self):
#         return f"Max speed is {self.max_speed}"
#
#     def run_car(self):
#         self.is_running = True
#
#     def __str__(self):  # Redefine object verbal representation.
#         return f"Is car running: {self.is_running}"
#
#     def __repr__(self):  # Redefine object verbal representation.
#         return f"REPR: Is car running: {self.is_running}"
#
#
# car = Vehicle(100, 35)
# car.run_car()
# print(car)

# --

# class Vehicle:
#     schema = "System"
#
#     def __init__(self, mileage, max_speed=150):
#         self.mileage = mileage
#         self.max_speed = max_speed
#         self.gadgets = []
#         self.is_running = False
#
#
# truck = Vehicle(1000, 130)
# truck2 = Vehicle(1002, 132)
# truck.schema = "Second System"
# print(truck.schema)
# print(truck2.schema)

# --

# class Dog:
#
#     tricks = []
#     voice = None
#
#     def __init__(self, breed):
#         self.breed = breed
#
#
# poodle = Dog("Poodle")
# sanbernar = Dog("Sanbernar")
# sanbernar.tricks.append("Give Pow")
# sanbernar.voice = "Loud"
# print(poodle.tricks)
# print(sanbernar.voice)
# print(poodle.voice)

# -- Class accepting *args

#
# class AcceptArgs:
#     letters = "abcdefghijklmnop"
#
#     def __init__(self, *args):
#         self.args = args
#         for item in args:
#             AcceptArgs.__setattr__(self, item, args.index(item))
#
#
# aa = AcceptArgs("one", "two", "three", "four", "five")
# print(aa.__dict__)

# -- Class attributes and Instance attributes are different

# class ClassInstancesDif:
#     c_container = [1]
#
#     def __init__(self, *args):
#         self.c_container = args
#
#     def __str__(self):
#         return str(self.c_container) + str(ClassInstancesDif.c_container)
#
#
# print(ClassInstancesDif(["A", "B"]))  # Class
# ci = ClassInstancesDif(["a", "b"])  # Instance
# print(ci)

# -- @staticmethod

# class StaticHolder:
#
#     def __init__(self, phrase: str):
#         self.phrase = phrase
#
#     @staticmethod
#     def stat_method():
#         return "Non related"
#
#
# sh = StaticHolder("Expression")
# print(sh.stat_method())

# -- the brackets after the class name makes the cursor look for the __init__ method

# class NoBracketed:
#     class_var = 1
#
#     def __init__(self, *args):
#         self.args = args
#
#
# nb = NoBracketed
# print(nb.class_var)
# # print(nb.args)  # does not know about the initialization(__init__)

# -- The super() method

# class Parent:
#
#     def __init__(self, student_1="John", student_2="Li"):
#         self.student_1 = student_1
#         self.student_2 = student_2
#
#     def students_present(self):
#         return [getattr(self, dict_item) for dict_item in self.__dict__]
#
#
# class Child(Parent):
#     def __init__(self, student_1="John", student_2="Li", student_3="Hose"):
#         super().__init__(student_1, student_2)
#         self.student_3 = student_3


# ch = Child()
# print(ch.students_present())

# -- Multilevel Inheritance

# class Parent:
#     def __init__(self, student_1):
#         self.student_1 = student_1
#
#     def __str__(self):
#         students = ", ".join([s for s in self.__dict__.values()])
#         return f"Our students are {students}."
#
#
# class Child(Parent):
#     def __init__(self, student_1, student_2):
#         super().__init__(student_1)
#         self.student_2 = student_2
#
#
# class GrandChild(Child):
#     def __init__(self, student_1, student_2, student_3):
#         super().__init__(student_1, student_2)
#         self.student_3 = student_3
#
#
# p = Parent("Pol")
# print(p)
# c = Child("Pol", "Azis")
# print(c)
# gc = GrandChild("Pol", "Azis", "Barakaguira")
# print(gc)

# -- Mixins Example


# class ListMixin:
#     def get_values(self):
#         values = [v for v in self.__dict__.values()]
#         return values
#
#
# class Employee(ListMixin):
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary
#
#
# e = Employee("Pier", 34000)
# print(e.get_values())

# -- Check inherited classes with __bases__

# class Parent:
#     def __init__(self, student_1):
#         self.student_1 = student_1
#
#     def __str__(self):
#         students = ", ".join([s for s in self.__dict__.values()])
#         return f"Our students are {students}."


# class Child(Parent):
#     def __init__(self, student_1, student_2):
#         super().__init__(student_1)
#         self.student_2 = student_2
#
#
# class GrandChild(Child):
#     def __init__(self, student_1, student_2, student_3):
#         super().__init__(student_1, student_2)
#         self.student_3 = student_3
#
#
# gc = GrandChild("N1", "N2", "N3")
# class_name = gc.__class__.__bases__[0].__name__
#
# print(class_name)
# # while class_name != "object":
# #     print(class_name)
# #     class_name = None

# -- Protected Variable

# class Puppy:
#     def __init__(self, name="Spooky"):
#         self._name = name
#
#
# san = Puppy("Ampi")
# print(san._name)  # Simply a recommendation

# -- Private Variables - child classes have no access to them

# class Parent:
#     def __init__(self, name: str="Peter"):
#         self.__name = name
#
#     def parent_property(self):
#         print(self.__name)
#
#
# class Child(Parent):
#     def present_property(self):
#         print(self.__name)  # The child class don't have access to privet parent variable.
#
# p = Parent("Jones")
# # print(p._Parent__name)
# c = Child("Okocha")
# c.parent_property()
# c.present_property()

# -- Combine getter and setter

# class Child:
#     def __init__(self, name: str):
#         self.name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if len(value) > 3:
#             value = value + "XXX"
#             self.__name = value
#         self.__name = value
#
#
# c = Child("Gabor")
# print(c.name)
# c.name = "Cristian"
# print(c.name)
# c.name = "Bo"
# print(c.name)

# -- Return on the getter a random data

# class Child:
#     def __init__(self, name: str):
#         self.name = name
#
#     @property
#     def name(self):
#         return "Somthing else"
#
#     @name.setter
#     def name(self, value):
#         if len(value) > 3:
#             value = value + "XXX"
#             self.__name = value
#         self.__name = value
#
#
# c = Child("Gabor")
# print(c.name)

# -- dunder method

# class Parent:
#     def __init__(self, name: str = "Tito"):
#         self.name = name
#
#     def __print_name(self):
#         return self.name
#
#
# p = Parent()
# print(p._Parent__print_name())
# # print(p.__print_name)  # Rises mistake

# setter that rises an error

# class Child:
#     def __init__(self, name: str):
#         self.name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if len(value) > 3:
#             value = value + "XXX"
#             self.__name = value
#         else:
#             raise ValueError("The value is to short!")
#
#
# c = Child("Tito")
# c.name = "Pe"
# print(c.name)

# -- getattr() method

# class Child:
#     def __init__(self, name: str):
#         self.name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if len(value) > 3:
#             value = value + "XXX"
#             self.__name = value
#         else:
#             raise ValueError("The value is to short!")
#
#
# c = Child("Tito")
# c_name = getattr(c, "name")
# print(c_name)

# Tyr to get all the inherited classes

# getattr() - setattr()

# class Child:
#     def __init__(self, name: str):
#         self.name = name
#         self.age = 12
#         self.father_name = "Ojos"
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if len(value) > 3:
#             value = value + "XXX"
#             self.__name = value
#         else:
#             raise ValueError("The value is to short!")
#
#
# c = Child("Kurt")
#
# items = {"Pen": 1, "Pencil": "Go", "Pencil Sharpener": 13}
# for item in items:
#     c.__setattr__(item, items[item] + 3 if type(items[item]) == int else items[item])
#
# print(c.__dict__)
# for prop in c.__dict__:
#     get_prop = getattr(c, prop)
#     print(get_prop)

# -- Get class attributes names as strings

# class Child:
#     def __init__(self, name: str):
#         self.name = name
#         self.age = 12
#         self.father_name = "Ojos"
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if len(value) > 3:
#             value = value + "XXX"
#             self.__name = value
#         else:
#             raise ValueError("The value is to short!")
#
#
# c = Child("Marina")
# for name in c.__dict__:
#     print(name)
#     get_item = getattr(c, name)
#     print(f"Got Item: {get_item}")

# -- Overwrite __setattr__() / make all assignments to equal "1"

# class Child:
#     def __init__(self, name: str):
#         self.name = name
#         self.age = 12
#         self.father_name = "Ojos"
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = 1
#
#
# c = Child("Tony")
# # c.new_attr = "NEW"
# print(c.__dict__)

# -- @property Test

from abc import ABC
#
#
class BaseClimber(ABC):
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

# --


