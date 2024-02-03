# Parking Lot


n = int(input())
cars_set = set()

for _ in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        cars_set.add(car_number)
    elif direction == "OUT":
        cars_set.remove(car_number)

if len(cars_set) > 0:
    {print(number) for number in cars_set}
else:
    print("Parking Lot is Empty")
