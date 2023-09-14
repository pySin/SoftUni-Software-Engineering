# hospital

# На първия ред – периода, за който трябва да направите изчисления. Цяло число в интервала [1 ... 1000]
# На следващите редове(равни на броят на дните) – броя пациенти, които пристигат за преглед за текущия
# ден. Цяло число в интервала [0…10 000]

period = int(input())
treated_patients = 0
untreated_patients = 0

number_of_doctors = 7

for i in range(1, period + 1):

    if i % 3 == 0:
        if treated_patients < untreated_patients:
            number_of_doctors += 1

    patients = int(input())

    if patients <= number_of_doctors:
        treated_patients += patients
    elif patients > number_of_doctors:
        treated_patients += number_of_doctors
        untreated_patients += patients - number_of_doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
