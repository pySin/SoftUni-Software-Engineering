# Clock

# for hour in range(24):
#     for minute in range(60):
#         print(f"{hour}:{minute}")

hour = 0
while hour < 24:
    for minute in range(60):
        print(f"{hour}:{minute}")
        break
    hour += 1
