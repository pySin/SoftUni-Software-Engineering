# Skeleton

# Минути на контролата – цяло число в интервала [0…59]
# Секунди на контролата – цяло число в интервала [0…59]
# Дължината на улея в метри – реално число в интервала [0.00…50000]
# Секунди за изминаване на 100 метра – цяло число в интервала [0…1000]

control_minutes = int(input())
control_seconds = int(input())
tube_meters = float(input())
seconds_per_100_meter = int(input())

whole_control_seconds = (control_minutes * 60) + control_seconds
marian_seconds = tube_meters * seconds_per_100_meter

current_position = 0
current_time_seconds = 0
decrease = 0

while current_position < tube_meters:
    current_position += 120
    #print(current_position)
    current_time_seconds += (seconds_per_100_meter * 1.20) - 2.5
    #print(current_time_seconds)
    # decrease += 2.5

remainder_meters = current_position - tube_meters
remainder_seconds = seconds_per_100_meter * (remainder_meters / 100)
# print(current_time_seconds)
# print(remainder_seconds)

time_result = current_time_seconds + remainder_seconds
# print(time_result)

if time_result < whole_control_seconds:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_result :.3f}.")
else:
    # print(f"{whole_control_seconds}, - {time_result}")
    print(f"No, Marin failed! He was {whole_control_seconds - time_result :.3f} second slower.")
