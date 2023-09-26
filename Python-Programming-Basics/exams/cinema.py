# Cinema

# На първия ред - капацитет на залата - цяло число в интервала [50... 150]
# На всеки следващ ред до команда "Movie time!":
# Брой хора влизащи в киното - цяло число в интервала [1… 15]

hall_capacity = int(input())
income = 0
hall_filled = 0

while True:

    number_of_people = input()

    if number_of_people == "Movie time!":
        print(f"There are {hall_capacity - hall_filled} seats left in the cinema.")
        print(f"Cinema income - {income} lv.")
        break

    number_of_people = int(number_of_people)
    hall_filled += number_of_people

    if hall_filled > hall_capacity:
        print(f"The cinema is full.")
        print(f"Cinema income - {income} lv.")
        break

    current_bill = number_of_people * 5

    if number_of_people % 3 == 0:
        current_bill -= 5

    income += current_bill
