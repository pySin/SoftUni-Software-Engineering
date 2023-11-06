# The Office

def office_happiness(employees_happy, factor):
    employees_happy = employees_happy.split(" ")
    happiness_increase = list(map(lambda x: int(x) * factor, employees_happy))
    filtered_happiness = list(filter(lambda x: x >= sum(happiness_increase) / len(happiness_increase),
                                     happiness_increase))
    return filtered_happiness, happiness_increase


workers_happiness = input()
improvement_factor = int(input())

happy_people = office_happiness(workers_happiness, improvement_factor)
if len(happy_people[0]) >= len(happy_people[1]) / 2:
    print(f"Score: {len(happy_people[0])}/{len(happy_people[1])}. Employees are happy!")
else:
    print(f"Score: {len(happy_people[0])}/{len(happy_people[1])}. Employees are not happy!")
