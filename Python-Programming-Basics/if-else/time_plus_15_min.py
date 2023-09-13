# Time + 15 min

hour = int(input())
minutes = int(input())

minutes += 15

x = 0
if hour == 23:
    x += 1

if minutes > 59:
    hour += 1
    minutes = minutes % 60
    x += 1

if x == 2:
    hour = 0

if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")
