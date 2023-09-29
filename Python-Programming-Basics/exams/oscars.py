# Oscars
ACCEPTANCE_POINTS = 1250.5

# Име на актьора – текст
# Точки от академията - реално число в интервала [2.0... 450.5]
# Брой оценяващи n – цяло число в интервала[1… 20]
# На следващите n-на брой реда:
# Име на оценяващия – текст
# Точки от оценяващия – реално число в интервала [1.0... 50.0]

actor_name = input()
points_from_academy = float(input())
number_of_jury = int(input())

actor_points = points_from_academy

for _ in range(number_of_jury):
    jury_name = input()
    jury_points = float(input())

    real_points = (len(jury_name) * jury_points) / 2
    actor_points += real_points

    if actor_points >= ACCEPTANCE_POINTS:
        break

if actor_points >= ACCEPTANCE_POINTS:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points :.1f}!")
else:
    print(f"Sorry, {actor_name} you need {ACCEPTANCE_POINTS - actor_points :.1f} more!")
