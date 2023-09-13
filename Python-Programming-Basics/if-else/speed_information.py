# Speed Information

speed_number = float(input())

if speed_number <= 10:
    print("slow")
elif speed_number <= 50:
    print("average")
elif speed_number <= 150:
    print("fast")
elif speed_number <= 1000:
    print("ultra fast")
else:
    print("extremely fast")
