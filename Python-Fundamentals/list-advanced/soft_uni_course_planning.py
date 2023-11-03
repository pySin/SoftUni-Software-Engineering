# Soft Uni Course planning
initial_schedule = input()


def course_plan(initial_lessons):
    lessons = initial_lessons.split(", ")
    # print(lessons)
    command = input()
    # print(command)
    while command != "course start":
        operations = command.split(":")
        if operations[0] == "Add":
            lessons.append(operations[1])
        elif operations[0] == "Insert":
            if operations[1] not in lessons:
                lessons.insert(int(operations[2]), operations[1])
        elif operations[0] == "Remove":
            # print("Op: " + operations[1])
            lessons.remove(operations[1])
        elif operations[0] == "Swap":
            # print(operations[0])
            # print(lessons.index(operations[1]))
            # print(lessons.index(operations[2]))
            # print(lessons)
            index_1 = lessons.index(operations[1])
            index_2 = lessons.index(operations[2])
            lessons[index_1], lessons[index_2] = lessons[index_2], lessons[index_1]
            # lessons[lessons.index(operations[1])], lessons[lessons.index(operations[2])] = \
            #     lessons[lessons.index(operations[2])], lessons[lessons.index(operations[1])]
            for i in range(len(lessons)):
                if "Exercise" in lessons[i]:
                    exercise_lesson = lessons[i]
                    lessons.pop(i)
                    lecture_index = lessons.index(exercise_lesson[:-9])
                    lessons.insert(lecture_index + 1, exercise_lesson)
            # print(lessons)
            # lessons[0], lessons[2] = lessons[2], lessons[0]
        elif operations[0] == "Exercise":
            if operations[1] in lessons:
                lecture_index = lessons.index(operations[1])
                lessons.insert(lecture_index + 1, operations[1] + "-" + operations[0])
            else:
                lessons.append(operations[1])
                lessons.append(operations[1] + "-" + operations[0])

        command = input()

    return lessons


lessons_order = 1
for lesson in course_plan(initial_schedule):
    print(f"{lessons_order}.{lesson}")
    lessons_order += 1
