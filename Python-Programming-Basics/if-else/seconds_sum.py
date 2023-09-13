# Sum the Seconds in time format

time_first = int(input())
time_second = int(input())
time_third = int(input())

summed_seconds = time_first + time_second + time_third
whole_minutes = summed_seconds // 60
seconds_left = summed_seconds % 60

if seconds_left < 10:
    print(f"{whole_minutes}:0{seconds_left}")
else:
    print(f"{whole_minutes}:{seconds_left}")
