# Average grade from education

student_name = input()
passed_years = 0
fail_in_a_row = 0

grades_sum = 0

while passed_years != 12:
    current_grade = float(input())

    if current_grade < 4:
        fail_in_a_row += 1
        if fail_in_a_row == 2:
            print(f"{student_name} has been excluded at {passed_years + 1} grade")
            break
        continue

    passed_years += 1
    grades_sum += current_grade

if passed_years == 12:
    print(f"{student_name} graduated. Average grade: {grades_sum / passed_years :.2f}")
