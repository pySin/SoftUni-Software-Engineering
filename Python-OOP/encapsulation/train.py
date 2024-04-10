# class Person:
#     kind = "mammal"
# 
#     def __init__(self, name: str, age: int):
#         self._name = name  # signifies Protected
#         self.age = age
#         self.__car = "Volvo"  # signifies Private
# 
#     def say_hi(self):
#         return "Hello"
# 
# 
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self._name = f"Student {name}"
# 
# 
# p = Person("Test", 30)
# print(p.age)
# # Name Mangling
# print(p._Person__car)
# p._Person__car = "Subaru"
# print(p._Person__car)

# --

# class Person:
#
#     def __init__(self, name, age=0):
#         self.name = name
#         self.__age = age
#
#     def info(self):
#         print(f"I am {self.name}, {self.__age} years old.")
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if age < 0:
#             raise ValueError("Age must be greater than 0")
#         self.__age = age
#
#
# p = Person("john", 33)
# print(p.get_age())
# p.set_age(-44)
# print(p.get_age())

# --

# class DebitCard:
#     def __init__(self, name_on_card, card_number, exp_date, cvv):
#         self.name_on_card = name_on_card
#         self.__card_number = self.set_card_number(card_number)
#         print(self.__card_number)
#         self.exp_date = exp_date
#         self.__cvv = cvv
#
#     def get_card_number(self):
#         return f"{'*' * 10} {str(self.__card_number)[-4:]}"
#
#     def set_card_number(self, new_card_number):
#         if len(str(new_card_number)) != 16:
#             raise ValueError("Card number must be exactly 16 digits!")
#         return str(new_card_number)
#
#     def get_cvv(self):
#         return "Contact your bank!"
#
#
# dc = DebitCard("TestUser", 1234567890123848, "2024-01", 666)
# print(dc.get_card_number())
# # dc.set_card_number(9876543219878)
# # print(dc.get_card_number())
# print(dc.get_cvv())

# --

# class Person:
#     def __init__(self, age=0):
#         self.age = age
#
#     @property
#     def age(self):
#         print("In Getter!")
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age < 18:
#             self.__age = 18
#         else:
#             self.__age = age
#
#
# p = Person(17)
# print(p.age)
# p.age = 12  # the Setter does not allow the value to be 12(@age.setter / def age...)
# print(p.age)
# p.age = 25
# print(p.age)
# print(p.age)
# print(p.age)

# --

# class Car:
#     def __init__(self, max_speed: int):
#         self.max_speed = max_speed
#
#     def drive(self):
#         print('driving max speed ' + str(self.max_speed))
#
#     @property
#     def max_speed(self):
#         return self.__max_speed
#
#     @max_speed.setter
#     def max_speed(self, value):
#         if value > 447:
#             value = 447
#         self.__max_speed = value
#
#
# red_car = Car(500)
# red_car.drive()  # driving max speed 200
# red_car.max_speed = 512  # changes the speed to 447 / the equal(=) sign triggers the SETTER
# red_car.drive()  # driving max speed 447


# --

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value <= 0:  # The value won't be set if the rule is not followed. Exception is thrown.
#             raise Exception("Age must be greater than zero")
#         self.__age = value
#
#
# p = Person("John", -33)  # The __init__ constructor calls the setter which throws error.

# --

# pass_w = "innffy6"
#
# if not any([letter.isdigit() for letter in pass_w]):
#     print(True)

# -- Method Name Mangling

# class Person:
#     def __init__(self):
#         self.first_name = 'Peter'
#         self.last_name = 'Parker'
#
#     def __full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def info(self):
#         return self.__full_name()
#
#
# p = Person()
# # print(p.__full_name)  # Raises NotFound
# print(p._Person__full_name())

# email = "pe77er@gmail.com"
# mail = email[email.index("@") + 1:][:email[email.index("@") + 1:].index(".")]
#
# print(mail)
# name = email[:email.index("@")]
# mail = email[email.index("@") + 1:][:email[email.index("@") + 1:].index(".")]
# domain = email[email.index("@") + 1:][email[email.index("@") + 1:].index(".") + 1:]
# print(name, mail, domain)

# --

# class Account:
#     def __init__(self, id, balance, pin):
#         self.balance = balance
#         self.__id = id
#         self.__pin = pin
#
#     def get_id(self, pin):
#         if pin == self.__pin:
#             return self.__id
#         return "Wrong pin"
#
#     def change_pin(self, old_pin, new_pin):
#         if old_pin == self.__pin:
#             self.__pin = new_pin
#             return "Pin changed"
#         return "Wrong pin"
#
#
# account = Account(23, 2345, 1111)
# print(getattr(account, "balance", "No such attribute!"))

# -- getattr() usage: returns attribute if found

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# person = Person("Peter")
# print(getattr(person, "name", "No person called Peter"))
# print(getattr(person, "name_x", "No person called Peter"))

# -- __getattr__  # called when getattr() is called
# It can be overwritten

# class Phone:
#     # size = 12
#
#     def __getattr__(self, attr):
#         if len(attr) > 5:
#             return attr
#         return "Value smaller than 5"
#         # return None
#
#     size = 12
#
#
# phone = Phone()
# p_size = phone.size
# print(p_size)
# print(getattr(phone, "size"))
# print(getattr(phone, "go"))
# print(getattr(phone, "sizeees"))

# --

# class Phone:
#     def __getattr__(self, attr):
#         if len(attr) > 5:
#             return attr
#         return "Method does not exist."
#
#
# phone = Phone()
# print(phone.boo)  # calling an attribute goes through __getattr__
# print(phone.gold)
# print(phone.non_existent)  # The called sub-attribute(non_existent) becomes the "attr"!

# -- hasattr()

# class DontHave:
#     def __init__(self):
#         self.some = 12
#
#
# dont = DontHave()
# print(hasattr(dont, "boo"))
# print(hasattr(dont, "some"))

# -- setattr()


# class Person:
#     def __init__(self):
#         self.name = "Peter"
#
#
# person = Person()
# person.new_attr = 14  # Uses the setattr() as well
# setattr(person, "age", 33)
# for i in range(10):
#     setattr(person, "a" + str(i), "value" + str(i))
# print(person.age)
# print(person.a1)
# print(person.__dict__)

# -- has dunder variant __setattr__

# class Phone:
#     def __setattr__(self, attr, value):
#         self.__dict__[attr] = value.upper()
#
#
# phone = Phone()
# phone.color = "black"
# print(phone.color)
# print(phone.__dict__)

# delattr()

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# person = Person("Peter")
# print(person.name)
# print(delattr(person, "name"))
# print(person.name)

# __delattr__() can be overwritten

# class Phone:
#     def __delattr__(self, attr):
#         del self.__dict__[attr]
#         print(f"'{str(attr)}' was deleted")
#
#
# phone = Phone()
# phone.color = "black"
# phone.color_2 = "Orange"
# del phone.color  # calls __delattr__()
# print(phone.__dict__)
# delattr(phone, "color_2")
# print(phone.__dict__)

# Name Mangling

# class Animal:
#     def __init__(self, class_a: str, name: str):
#         self.__class_a = class_a
#         self.__name = name
#
#     def animal_data(self):
#         return f"{self.__name} is of class {self.__class_a}"
#
#
# a = Animal("Cats", "Pietro")
# print(a._Animal__class_a)
# # print(a.__name)

# --

# class Animal:
#     def __init__(self, class_a: str, name: str):
#         self.class_a = class_a
#         self.name = name
#
#     @property
#     def class_a(self):
#         return self.__class_a
#
#     @class_a.setter
#     def class_a(self, class_a):
#         print("Setting Animal")
#         self.__class_a = class_a
#
#
# cat = Animal("cats", "Moritz")
# print(cat.class_a)
# cat.class_a = "Maco"
# print(cat.class_a)

# elements = [1, 2, 3, 4]
# removed = elements.pop(1)
# print(removed)


# -- Encapsulation

# class ManyProperties:
#
#     def __init__(self, name: str):
#         self.name = name
#
#
# mp = ManyProperties("Jules")
# print(mp.__dict__)
#
# for num in range(12):
#     mp.__setattr__(str(num) + "a", num)
#
# print(mp.__dict__)


# - Staticmethod

# class CheckVar:
#
#     def __init__(self):
#         self.var = 1
#
#     @staticmethod
#     def check_access(var):
#         print(var)
#
#
# cv = CheckVar()
# cv.check_access(cv.var)

# --

# class CheckIt:
#     def __init__(self, name: str):
#         self.__name = name


# ci = CheckIt("Ogi")
# print(ci._CheckIt__name)  # Name Mangling

# -- private functions

# class PrivateMethods:
#
#     def __init__(self, name: str):
#         self.name = name
#
#     def __print_name(self):
#         print(self.name)
#
#
# pm = PrivateMethods("Ros")
# pm._PrivateMethods__print_name()  # Mangled class Function name

# -- setattr()

# class SA:
#     pass
#
#
# sa = SA()
#
# keys_words = [("shoes", 34), ("clothes", 12), ("Hat", 8)]
#
# for belonging in keys_words:
#     setattr(sa, belonging[0], belonging[1])
#
# print(sa.shoes)
# print(sa.clothes)
# print(sa.Hat)

# --
