# Test File

# keys = ["name", "age", "major"]
# values = ["Ivan", 25, "Computer Science"]
#
# student = {}
#
# for i in range(len(keys)):
#     student[keys[i]] = values[i]
#
# print(student)

# student = dict('name'='Ivan')  # "age"=26, "major"="Computer Science")

# student = dict(name="Ivan", age=25, major="Computer Science")
# student = dict([("name", "ivan"), ("age", 25), ("occupation", "Developer")])
#
# print(student)


# -- ZIP

# keys = ["name", "age", "major"]
# values = ["ivan", 35, "Computer Science"]
#
# student = dict(zip(keys, values))
# print(student)
# print(student.get("age"))
# print(student.get("age1"))  # Get doesn't rase exception.

# Change values iterating through keys

# squares = {1: 1, 2: 4, 3: 9}
# for key in squares.keys():
#     squares[key] *= 2
#
# print(squares)

# squares = {1: 1, 2: 4, 13: 9}
#
# for k in squares:"
#     print(k)
#     print(squares[k])

# student = {
#     "name": "Prikshit",
#     "age": 27,
#     "major": "Computers",
#     "gpa": 4.7
# }
#
# if "Computers" in student.values():
#     print("Computers exists in Students major")
# else:
#     print("No Computers")
#
# for key, value in student.items():
#     if value == "Computers":
#         print(f"{value}\'s key is: {key}")

# -- len() of dictionary
# student = {
#     "name": "Prikshit",
#     "age": 27,
#     "major": "Computers",
#     "gpa": 4.7
# }
#
# print("Student metrics: " + str(len(student)))

# -- update()

# student = {
#     "name": "Prikshit",
#     "age": 27,
#     "major": "Computers",
#     "gpa": 4.7
# }
#
# student_2 = {
#     "name1": "Gruhi",
#     "age1": 34,
#     "major1": "Computers",
#     "gpa1": 4.9
# }
#
# student.update(student_2)
# print(student)

# -- Nested Dictionaries

# students = {
#     "Gosho": {"Math": 5, "Science": 6, "English": 6},
#     "Pesho": {"Math": 4, "Science": 6, "English": 6},
#     "Maria": {"Math": 6, "Science": 6, "English": 5}
# }
#
# for student, record in students.items():
#     # print(student, record)
#     print("\n" + student)
#     for subject, score in record.items():
#         print(subject + " - " + str(score))

# print(students)
# print(students["Gosho"])
# print(students["Maria"])
# print(students["Maria"]["Math"])
# students["Gosho"]["Math"] += 3
# print(students["Gosho"])
# students["Gosho"]["Fisical"] = 5
# print(students["Gosho"])

# -- Dictionary Comprehension

# data = [("Peter", 22), ("Amy", 18), ("George", 35)]
# dictionary = {key: value for (key, value) in data}
# print(dictionary)
#
# nums = [1, 2, 3]
# dictionary_2 = {num: num ** 3 for num in nums}
# print(dictionary_2)


# -- Empty value Dictionary

# dict_1 = {"Item 1": None}
# print(dict_1)


