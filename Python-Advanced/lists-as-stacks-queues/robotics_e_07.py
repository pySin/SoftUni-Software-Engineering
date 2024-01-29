# Robotics
# from collections import deque
# from datetime import datetime, timedelta
#
# robots_data = [(x.split("-")[0], int(x.split("-")[1])) for x in input().split(";")]
# starting_time = input()
# time_string = f"2023-10-24 {starting_time}"
# real_current_time = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
#
#
# command = input()
# available_robots = deque(robots_data)
# working_robots = {name: 0 for name, op_time in robots_data}
# seconds = 0
# product_queue = deque()
#
# while True:
#     seconds += 1
#     product = command
#     if command == "End":
#         if len(product_queue) > 0:
#             product = product_queue[0]
#
#     for robot in robots_data:
#         robot_name = robot[0]
#         process_time = robot[1]
#         if robot_name in working_robots:
#             if working_robots[robot_name] == seconds:
#                 available_robots.append(robot)
#                 # working_robots[robot_name] = seconds + process_time
#
#     if len(available_robots) < 1:
#         product_queue.append(product)
#         product_queue.rotate()
#         if command == "End":
#             continue
#         else:
#             command = input()
#             continue
#     else:
#         time_delta = timedelta(seconds=seconds)
#         current_time = real_current_time + time_delta
#         # print(current_time)
#         first_available_robot = available_robots.popleft()
#         working_robots[first_available_robot[0]] = first_available_robot[1] + seconds
#         print(f"{first_available_robot[0]} - {product} [{str(current_time)[-8:]}]")
#         if len(product_queue) > 0:
#             product_queue.popleft()
#         if command == "End" and len(product_queue) < 1:
#             break

    # command = input()


# ---

# Robotics
# from collections import deque
# from datetime import datetime, timedelta
#
# robots_data = [(x.split("-")[0], int(x.split("-")[1])) for x in input().split(";")]
# starting_time = input()
# time_string = f"2023-10-24 {starting_time}"
# real_current_time = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
#
#
# command = input()
# available_robots = deque(robots_data)
# working_robots = {name: 0 for name, op_time in robots_data}
# seconds = 0
# product_queue = deque()
#
# while True:
#     seconds += 1
#
#     for robot in robots_data:
#         robot_name = robot[0]
#         process_time = robot[1]
#         if robot_name in working_robots:
#             if working_robots[robot_name] == seconds:
#                 available_robots.append(robot)
#
#     if len(available_robots) < 1:
#         if command == "End":
#             if len(product_queue) < 1:
#                 break
#             else:
#                 pass
#                 product_queue.rotate(-1)
#         else:
#             product_queue.append(command)
#
#     else:
#         if command == "End":
#             if len(product_queue) < 1:
#                 break
#             else:
#                 product = product_queue.popleft()
#         else:
#             product = command
#         time_delta = timedelta(seconds=seconds)
#         current_time = real_current_time + time_delta
#         first_available_robot = available_robots.popleft()
#         working_robots[first_available_robot[0]] = first_available_robot[1] + seconds
#         print(f"{first_available_robot[0]} - {product} [{str(current_time)[-8:]}]")
#
#     if command != "End":
#         command = input()


# -- Atanas Atanasov's solution

from collections import deque


products = deque()
robots = []
robots_data = input().split(";")

hours, minutes, seconds = [int(x) for x in input().split(":")]
start_time_seconds = hours * 3600 + minutes * 60 + seconds

for robot in robots_data:
    robot_name, processing_time = robot.split("-")
    busy_until_time = 0
    robots.append({"name": robot_name, "data": [int(processing_time), busy_until_time]})

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    start_time_seconds += 1
    current_product = products.popleft()
    is_taken = False

    for robot in robots:
        if robot["data"][1] <= start_time_seconds:
            robot["data"][1] = start_time_seconds + robot["data"][0]
            h = start_time_seconds // 3600
            m = (start_time_seconds % 3600) // 60
            s = (start_time_seconds % 3600) % 60
            h = h % 24
            print(f"{robot['name']} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
            is_taken = True
            break

    if not is_taken:
        products.append(current_product)
