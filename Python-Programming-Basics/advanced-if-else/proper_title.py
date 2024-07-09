# Proper Title

age = float(input())
gender = input()
title = ""

if gender == "m":
    if age >= 16:
        title = "Mr."
    elif 0 <= age < 16:
        title = "Master"
elif gender == "f":
    if age >= 16:
        title = "Ms."
    elif 0 <= age < 16:
        title = "Miss"

print(title)
