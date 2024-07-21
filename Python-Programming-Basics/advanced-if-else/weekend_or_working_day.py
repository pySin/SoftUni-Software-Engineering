# Weekend or working day

day_name = input()
day_type = ""

if day_name == "Monday" or \
        day_name == "Tuesday" or \
        day_name == "Wednesday" or \
        day_name == "Thursday" or \
        day_name == "Friday":
    day_type = "Working day"
elif day_name == "Saturday" or day_name == "Sunday":
    day_type = "Weekend"
else:
    print("Error")

print(f"{day_type}")
