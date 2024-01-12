# SoftUni Reception 2

receptionist_1 = int(input())
receptionist_2 = int(input())
receptionist_3 = int(input())

number_of_students = int(input())
whole_clients_per_hour = receptionist_1 + receptionist_2 + receptionist_3

hours = number_of_students // whole_clients_per_hour
hours_rest = hours // 3

if number_of_students % whole_clients_per_hour != 0:
    hours += 1

if hours == 0:
    pass
elif hours % 3 == 0:
    hours_rest -= 1


print(f"Time needed: {hours + hours_rest}h.")
