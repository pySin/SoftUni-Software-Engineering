# Student academy

def grade_manage(name, grade, student_grades):
    if name in student_grades:
        student_grades[name] = (student_grades[name] + grade) / 2
    else:
        student_grades[name] = grade
    return student_grades


def call_functions():
    student_grades = {}

    n = int(input())
    average_grade = 4.50

    for _ in range(n):

        name = input()
        grade = float(input())

        student_grades = grade_manage(name, grade, student_grades)

    for student in student_grades:
        if student_grades[student] >= average_grade:
            print(f"{student} -> {student_grades[student]:.2f}")
    # print(student_grades)


if __name__ == "__main__":
    call_functions()
