# Soft Uni course planing


schedule_of_lessons = input().split(", ")


command = input()

while command != "course start":

    instructions = command.split(":")

    if instructions[0] == "Add":
        for course_name in schedule_of_lessons:
            if instructions[1] in course_name:
                break
            elif course_name == schedule_of_lessons[-1]:
                schedule_of_lessons.append(instructions[1])
                break
    elif instructions[0] == "Insert":
        for course_name in schedule_of_lessons:
            if instructions[1] in course_name:
                break
            elif course_name == schedule_of_lessons[-1]:
                schedule_of_lessons.insert(int(instructions[2]), instructions[1])
                break

    elif instructions[0] == "Remove":
        for course_name in schedule_of_lessons:
            if instructions[1] in course_name:
                schedule_of_lessons.remove(course_name)
                break
    elif instructions[0] == "Swap":
        swap_indexes = []
        for g in range(len(schedule_of_lessons)):
            if instructions[1] in schedule_of_lessons[g] or \
                    instructions[2] in schedule_of_lessons[g]:
                swap_indexes.append(g)

        if len(swap_indexes) == 2:
            schedule_of_lessons[swap_indexes[0]], schedule_of_lessons[swap_indexes[1]] = \
                schedule_of_lessons[swap_indexes[1]], schedule_of_lessons[swap_indexes[0]]
    elif instructions[0] == "Exercise":
        for i in range(len(schedule_of_lessons)):
            if schedule_of_lessons[i] == instructions[1]:
                schedule_of_lessons[i] += "-Exercise"
                break
            elif i == len(schedule_of_lessons) - 1:
                schedule_of_lessons.append(instructions[1] + "-Exercise")
                break

    command = input()

for j in range(len(schedule_of_lessons) - 1, - 1, - 1):
    if "Exercise" in schedule_of_lessons[j]:
        schedule_of_lessons.insert(j, schedule_of_lessons[j][:-9])

for f in range(len(schedule_of_lessons)):
    print(f"{f + 1}.{schedule_of_lessons[f]}")
