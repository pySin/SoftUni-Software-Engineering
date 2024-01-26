# Key Revolver
from collections import deque


def mission():
    bullet_price = int(input())
    barrel_size = int(input())
    bullets = [int(bullet) for bullet in input().split()]
    locks = deque([int(bullet) for bullet in input().split()])
    intelligence_value = int(input())
    money_spent = 0
    bullets_shot = 0

    while locks:
        current_lock = locks.popleft()
        while bullets:
            current_bullet = bullets.pop()
            money_spent += bullet_price
            bullets_shot += 1
            # if bullets_shot % barrel_size == 0:
            #     print("Reloading!")
            if current_bullet <= current_lock:
                print("Bang!")
                if not locks:
                    if bullets_shot % barrel_size == 0 and bullets:
                        print("Reloading!")
                    return f"{len(bullets)} bullets left. Earned ${intelligence_value - money_spent}"
                elif not bullets:
                    locks.appendleft(current_lock)
                    return f"Couldn't get through. Locks left: {len(locks)}"
                if bullets_shot % barrel_size == 0:
                    print("Reloading!")
                break
            else:
                print("Ping!")
                if not bullets:
                    locks.appendleft(current_lock)
                    return f"Couldn't get through. Locks left: {len(locks)}"
                if bullets_shot % barrel_size == 0:
                    print("Reloading!")
                continue


if __name__ == "__main__":
    print(mission())
