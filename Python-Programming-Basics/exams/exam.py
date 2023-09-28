# Exam

# На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]


students_count = int(input())

all_marks = 0
marks_sum = 0
over_5_marks = 0
between_4_5_marks = 0
between_3_4_marks = 0
less_3_marks = 0

for _ in range(students_count):
    current_mark = float(input())
    all_marks += 1

    marks_sum += current_mark
    if current_mark >= 5:
        over_5_marks += 1
    elif 4 <= current_mark < 5:
        between_4_5_marks += 1
    elif 3 <= current_mark < 4:
        between_3_4_marks += 1
    elif current_mark < 3:
        less_3_marks += 1

print(f"Top students: {(over_5_marks / all_marks) * 100 :.2f}%")
print(f"Between 4.00 and 4.99: {(between_4_5_marks / all_marks) * 100 :.2f}%")
print(f"Between 3.00 and 3.99: {(between_3_4_marks / all_marks) * 100 :.2f}%")
print(f"Fail: {(less_3_marks / all_marks) * 100 :.2f}%")
print(f"Average: {marks_sum / students_count :.2f}")
