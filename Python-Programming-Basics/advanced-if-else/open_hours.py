# Open Hours

hour = int(input())
day = input()

working_hour = ""

if day == "Monday" \
        or day == "Tuesday" \
        or day == "Wednesday" \
        or day == "Thursday" \
        or day == "Friday" \
        or day == "Saturday":
    if 10 <= hour <= 18:
        working_hour = "open"
    else:
        working_hour = "closed"
else:
    working_hour = "closed"

print(working_hour)
