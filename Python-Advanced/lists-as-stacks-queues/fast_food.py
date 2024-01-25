# Fast Food
from collections import deque


def get_data():
    food_quantity = int(input())
    queue_for_food = deque()
    [queue_for_food.append(int(num)) for num in input().split()]
    return food_quantity, queue_for_food


def find_biggest_order(queue):
    print(max(queue))


def serve_orders(food, queue):

    for _ in range(len(queue)):
        if queue[0] <= food:
            food -= queue[0]
            queue.popleft()
        else:
            break
    return queue


def call_functions():
    available_food, food_queue = get_data()
    find_biggest_order(food_queue)
    orders = serve_orders(available_food, food_queue)
    if orders:
        orders_left = ""
        for i in range(len(orders)):
            orders_left += str(orders.popleft()) + " "
        print(f"Orders left: {orders_left[:-1]}")
    else:
        print("Orders complete")


if __name__ == "__main__":
    call_functions()
