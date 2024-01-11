# Soft Uni Reception


receptionist_1 = int(input())
receptionist_2 = int(input())
receptionist_3 = int(input())

number_of_students = int(input())

students_per_hour = receptionist_1 + receptionist_2 + receptionist_3
hours_needed = 0
# hours_rest = 0

while True:

    if number_of_students > students_per_hour:
        hours_needed += 1
        number_of_students -= students_per_hour
        # if hours_needed % 3 == 0:
        #     hours_rest += 1
    elif number_of_students == students_per_hour:
        hours_needed += 1
        break
    elif number_of_students < students_per_hour:
        # if hours_needed % 3 == 0:
        #     hours_rest += 1
        hours_needed += 1
        break

hours_rest = hours_needed // 3
print(f"Time needed: {hours_needed + hours_rest}h.")
