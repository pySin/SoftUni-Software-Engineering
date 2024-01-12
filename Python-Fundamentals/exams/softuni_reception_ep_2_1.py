# Softuni Reception
# Get the input for each employee effectiveness and the count of students.
# Find the number of students served for an hour by all the employees.
# Find how many breaks the employees will have.
# Find the serving hours needed.
# Combine the serving hours with the breaks.
# Print the result.

employee_1_visitors_per_hour = int(input())
employee_2_visitors_per_hour = int(input())
employee_3_visitors_per_hour = int(input())

students_amount = int(input())


def time_needed(employee_1, employee_2, employee_3, students_count):
    served_students_per_hour = employee_1 + employee_2 + employee_3
    employees_breaks = students_count // (served_students_per_hour * 3)
    working_hours = students_count // served_students_per_hour
    if students_count % served_students_per_hour != 0:
        working_hours += 1

    sum_working_hours = working_hours + employees_breaks
    return f"Time needed: {sum_working_hours}h."


if __name__ == '__main__':
    phrase = time_needed(employee_1_visitors_per_hour, employee_2_visitors_per_hour,
                         employee_3_visitors_per_hour, students_amount)

    print(phrase)
