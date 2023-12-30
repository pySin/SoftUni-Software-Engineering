# Bonus Scoring System


number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

student_attendances = []

for _ in range(number_of_students):
    student_attendances.append(int(input()))

if len(student_attendances) > 0:
    best_attendant = max(student_attendances)
else:
    best_attendant = 0

if number_of_lectures > 0:
    total_bonus = round((best_attendant / number_of_lectures) * (5 + additional_bonus))
else:
    total_bonus = 0

print(f"Max Bonus: {total_bonus}.")
print(f"The student has attended {best_attendant} lectures.")
