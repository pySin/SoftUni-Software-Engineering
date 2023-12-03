class Person:

    # Class Attributes
    species = "Human"

    def __init__(self, name):
        self.name = name


person_1 = Person("Mustafa")
person_2 = Person("Baraka")

print(person_1.species)
print(person_2.species)

Person.species = "Homo sapiens"

print(person_1.species)
print(person_2.species)

person_1.species = "Homo Erectus"

print(person_1.species)
print(person_2.species)
