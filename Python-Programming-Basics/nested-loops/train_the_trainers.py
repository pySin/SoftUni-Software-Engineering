# Train the trainers

juries_count = int(input())

students_score_sum = 0
students_score_count = 0

command = input()
while command != "Finish":
    presentation_name = command

    student_mark = 0
    for mark in range(juries_count):
        current_mark = float(input())
        student_mark += current_mark
    student_score = student_mark / juries_count
    students_score_sum += student_score
    students_score_count += 1
    print(f"{presentation_name} - {student_score:.2f}.")

    command = input()

average_score = students_score_sum / students_score_count
print(f"Student's final assessment is {average_score:.2f}.")
