# Oscars

# ⦁	Име на актьора - текст
# ⦁	Точки от академията - реално число в интервала [2.0... 450.5]
# ⦁	Брой оценяващи n - цяло число в интервала[1… 20]
# На следващите n-на брой реда:
# ⦁	Име на оценяващия - текст
# ⦁	Точки от оценяващия - реално число в интервала [1.0... 50.0]

actor_name = input()
academy_points = float(input())
numer_of_juries = int(input())

actor_points = 0

for _ in range(numer_of_juries):
    jury_name = input()
    current_jury_points = float(input())
    current_points = (len(jury_name) * current_jury_points) / 2
    actor_points += current_points

    if actor_points + academy_points >= 1250.5:
        break

actor_points += academy_points

if actor_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points :.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - actor_points :.1f} more!")
