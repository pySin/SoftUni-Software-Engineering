# Truck tour
# from collections import deque
#
#
# petrol_pumps_count = int(input())
#
# petrol_stations = deque()
# distances = deque()
#
# for i in range(petrol_pumps_count):
#     current_station = [int(x) for x in input().split()]
#     petrol_stations.append(current_station[0])
#     distances.append(current_station[1])
#
# print(petrol_stations)
# print(distances)
#
# liters_of_petrol = 0
# # distance_possible = 0
# petrol_in_reach = 0
# initial_index = 0
# current_index = 0
#
# while True:
#
#     liters_of_petrol += petrol_stations[0]
#
#     if liters_of_petrol < distances[0]:
#         liters_of_petrol = 0
#         petrol_stations.append(petrol_stations.popleft())
#         distances.append(distances.popleft())
#         current_index += 1
#         continue
#
#     if liters_of_petrol >= distances[0]:
#         petrol_in_reach += 1
#         if petrol_in_reach == 1:
#             initial_index = current_index
#         petrol_stations.append(petrol_stations.popleft())
#         distances.append(distances.popleft())
#
#     if petrol_in_reach == len(distances) - 1:
#         print(initial_index)
#         break
#
#     current_index += 1

# -------- Atanas Atanasov

from collections import deque

n = int(input())

pumps = deque()
start_position = 0
stops = 0

for _ in range(n):
    current_fuel, distance = input().split()
    pumps.append([int(current_fuel), int(distance)])

while stops < n:
    fuel = 0
    for i in range(n):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= destination
        stops += 1

print(start_position)
