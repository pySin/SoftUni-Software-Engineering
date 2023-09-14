# Grades

# На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]

students_count = int(input())

grades_between_2_3 = 0
grades_between_3_4 = 0
grades_between_4_5 = 0
grades_between_5_6 = 0

grades_sum = 0

for _ in range(students_count):
    current_grade = float(input())
    grades_sum += current_grade

    if 2 <= current_grade < 3:
        grades_between_2_3 += 1
    elif 3 <= current_grade < 4:
        grades_between_3_4 += 1
    elif 4 <= current_grade < 5:
        grades_between_4_5 += 1
    elif current_grade >= 5:
        grades_between_5_6 += 1

print(f"Top students: {(grades_between_5_6 / students_count) * 100 :.2f}%")
print(f"Between 4.00 and 4.99: {(grades_between_4_5 / students_count) * 100 :.2f}%")
print(f"Between 3.00 and 3.99: {(grades_between_3_4 / students_count) * 100 :.2f}%")
print(f"Fail: {(grades_between_2_3 / students_count) * 100 :.2f}%")
print(f"Average: {grades_sum / students_count :.2f}")
