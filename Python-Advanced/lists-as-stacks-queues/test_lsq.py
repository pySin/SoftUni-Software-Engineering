# Test - Lists as Stacks and Queues


# stack = []
#
# stack.append(5)
# stack.append(10)
# stack.append(2)
#
# while stack:  # Prevents pop() from empty stack error
#     print(stack)
#     print(stack.pop())


# --

# stack = []
#
# for i in range(1, 10000000):
#     stack.append(i)
#
# print(stack.pop(0))


# --- Queue

# from collections import deque
#
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.append("Graham")
# print(queue)
# queue.popleft()
# queue.popleft()
# print(queue)

# --

# from collections import deque
#
# our_queue = deque()
#
# for i in range(20):
#     our_queue.appendleft(i)
#
# print(our_queue)
# our_queue.popleft()
# print(our_queue)


#  The workflow pro

# list_1 = [1, 2, 3]
#
# while list_1:
#     print(list_1.pop(), end="")
#     if list_1:
#         print("", end=", ")


# --------------

# receptionist_1 = int(input())
# receptionist_2 = int(input())
# receptionist_3 = int(input())
#
# number_of_students = int(input())
# whole_clients_per_hour = receptionist_1 + receptionist_2 + receptionist_3
#
# hours = number_of_students // whole_clients_per_hour
# hours_rest = hours // 3
#
# if number_of_students % whole_clients_per_hour != 0:
#     hours += 1
#
# if hours == 0:
#     pass
# elif hours % 3 == 0:
#     hours_rest -= 1
#
#
# print(f"Time needed: {hours + hours_rest}h.")

# from collections import deque
#
# x1 = deque([])
# x1.appendleft(1)
# x1.appendleft(2)
#
# print(x1)

# from collections import deque

# x = deque([1, 2, 5, 3])
# print(max(x))
# x.rotate(-1)
# print(x)
# y = deque({1: 2, 3: 4, 5: 6})
# print(y)

# ---

# from collections import deque
#
# x = deque({1: 2, 3: 4}.items())
# print(x)

from collections import deque

x = deque([1, 2, 3, 4])
x.rotate()
print(x)
