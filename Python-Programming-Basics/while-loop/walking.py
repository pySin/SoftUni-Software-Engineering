# Walking

goal_steps = 10000
steps_walked = 0


goal_not_reached = False
while goal_steps > steps_walked:

    initial_steps = input()

    if initial_steps == "Going home":
        current_steps = int(input())
        steps_walked += current_steps
        if steps_walked < goal_steps:
            goal_not_reached = True
        break

    current_steps = int(initial_steps)
    steps_walked += current_steps


if goal_not_reached:
    print(f"{goal_steps - steps_walked} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!")
    print(f"{steps_walked - goal_steps} steps over the goal!")
