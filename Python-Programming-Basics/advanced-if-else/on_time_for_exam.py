# On Time For Exam

# ⦁	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# ⦁	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# ⦁	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# ⦁	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.

exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

combined_exam_minutes = (exam_hour * 60) + exam_minute
combined_arrival_minutes = (arrival_hour * 60) + arrival_minute

difference = combined_exam_minutes - combined_arrival_minutes

if difference == 0:
    print(f"On time")
elif 0 < difference <= 30:
    print("On time")
    print(f"{difference} minutes before the start")
elif 30 < difference < 60:
    print("Early")
    print(f"{difference} minutes before the start")
elif difference >= 60:
    hours_difference = difference // 60
    print("Early")
    minutes_difference = difference % 60
    if minutes_difference < 10:
        print(f"{hours_difference}:0{minutes_difference} hours before the start")
    elif minutes_difference >= 10:
        print(f"{hours_difference}:{minutes_difference} hours before the start")
elif difference < 0:
    print("Late")
    hours_difference = abs(difference) // 60
    minutes_difference = abs(difference) % 60
    if difference <= -60:
        if minutes_difference < 10:
            print(f"{hours_difference}:0{minutes_difference} hours after the start")
        elif minutes_difference >= 10:
            print(f"{hours_difference}:{minutes_difference} hours after the start")
    elif difference > -60:
        print(f"{abs(difference)} minutes after the start")
