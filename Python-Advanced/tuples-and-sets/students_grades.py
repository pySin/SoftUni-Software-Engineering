# Students Grades


# students_count = int(input())
#
# student_grades = {}
#
# for _ in range(students_count):
#     name, grade = input().split()
#
#     if name in student_grades:
#         student_grades[name][1].append(grade)
#     else:
#         student_grades[name] = (name, [grade])
#
# for name in student_grades:
#     print(f"{student_grades[name][0]} -> {' '.join(map(str, student_grades[name][1]))}"
#           f" (avg: {sum(map(float, student_grades[name][1])) / len(student_grades[name][1]) :.2f})")


# Ines Solution

n = int(input())

students = {}

for i in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student_name, grades in students.items():
    formatted_grades = ' '.join([f"{grade:.2f}" for grade in grades])
    print(f"{student_name} -> {formatted_grades}"
          f" (avg: {sum(grades)/len(grades):.2f})")
