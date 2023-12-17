# Soft Uni course planing


# schedule_of_lessons = input().split(", ")
#
#
# command = input()
#
# while command != "course start":
#
#     instructions = command.split(":")
#
#     if instructions[0] == "Add":
#         if instructions[1] not in schedule_of_lessons:
#             schedule_of_lessons.append(instructions[1])
#     elif instructions[0] == "Insert":
#         if instructions[1] not in schedule_of_lessons:
#             schedule_of_lessons.insert(int(instructions[2]), instructions[1])
#     elif instructions[0] == "Remove":
#         for course_name in schedule_of_lessons:
#             if instructions[1] in course_name:
#                 schedule_of_lessons.remove(course_name)
#     elif instructions[0] == "Swap":
#         first_index = schedule_of_lessons.index(instructions[1])
#         second_index = schedule_of_lessons.index(instructions[2])
#
#         first_index_group = []
#         second_index_group = []
#
#         if schedule_of_lessons[first_index + 1] == instructions[1] + "-Exercise":
#             first_index_group.append(schedule_of_lessons[first_index])
#             first_index_group.append(schedule_of_lessons[first_index + 1])
#         else:
#             first_index_group.append(schedule_of_lessons[first_index])
#
#         if second_index == len(schedule_of_lessons) - 1:
#             second_index_group.append(schedule_of_lessons[second_index])
#         elif schedule_of_lessons[second_index + 1] == instructions[2] + "-Exercise":
#             second_index_group.append(schedule_of_lessons[second_index])
#             second_index_group.append(schedule_of_lessons[second_index + 1])
#         else:
#             second_index_group.append(schedule_of_lessons[second_index])
#
#         schedule_of_lessons[first_index], schedule_of_lessons[second_index] = \
#             schedule_of_lessons[second_index], schedule_of_lessons[first_index]
#
#         if len(first_index_group) == 2 == len(second_index_group):
#             schedule_of_lessons[first_index + 1], schedule_of_lessons[second_index + 1] = \
#                 schedule_of_lessons[second_index + 1], schedule_of_lessons[first_index + 1]
#
#         if len(first_index_group) == 1 and len(second_index_group) == 2:
#             schedule_of_lessons.insert(first_index + 1, schedule_of_lessons.pop(second_index + 1))
#
#         if len(first_index_group) == 2 and len(second_index_group) == 1:
#             schedule_of_lessons.insert(second_index + 1, first_index_group[1])
#             schedule_of_lessons.pop(first_index + 1)
#
#     elif instructions[0] == "Exercise":
#         for i in range(len(schedule_of_lessons)):
#             if schedule_of_lessons[i] == instructions[1] and \
#                     schedule_of_lessons[i + 1] != instructions[1] + "-Exercise":
#                 schedule_of_lessons.insert(i + 1, instructions[1] + "-Exercise")
#                 break
#             elif i == len(schedule_of_lessons) - 1:
#                 schedule_of_lessons.append(instructions[1])
#                 schedule_of_lessons.append(instructions[1] + "-Exercise")
#                 break
#
#     command = input()
#
# # for j in range(len(schedule_of_lessons) - 1, - 1, - 1):
# #     if "Exercise" in schedule_of_lessons[j]:
# #         schedule_of_lessons.insert(j, schedule_of_lessons[j][:-9])
#
# for f in range(len(schedule_of_lessons)):
#     print(f"{f + 1}.{schedule_of_lessons[f]}")


# ---|---

# schedule_of_lessons = input().split(", ")
#
#
# command = input()
#
# while command != "course start":
#
#     instructions = command.split(":")
#
#     if instructions[0] == "Add":
#         if instructions[1] not in schedule_of_lessons:
#             schedule_of_lessons.append(instructions[1])
#     elif instructions[0] == "Insert":
#         if instructions[1] not in schedule_of_lessons:
#             schedule_of_lessons.insert(int(instructions[2]), instructions[1])
#     elif instructions[0] == "Remove":
#         for course_name in schedule_of_lessons:
#             if instructions[1] in course_name:
#                 schedule_of_lessons.remove(course_name)
#     elif instructions[0] == "Swap":
#         command = input()
#         continue
#         # first_index = schedule_of_lessons.index(instructions[1])
#         # second_index = schedule_of_lessons.index(instructions[2])
#
#         # schedule_of_lessons[first_index], schedule_of_lessons[second_index] = \
#         #     schedule_of_lessons[second_index], schedule_of_lessons[first_index]
#
#     elif instructions[0] == "Exercise":
#         for i in range(len(schedule_of_lessons)):
#             if schedule_of_lessons[i] == instructions[1]:
#                 schedule_of_lessons[i] += "-Exercise"
#                 break
#             elif i == len(schedule_of_lessons) - 1:
#                 schedule_of_lessons.append(instructions[1] + "-Exercise")
#                 break
#
#     command = input()
#
# for f in range(len(schedule_of_lessons)):
#     print(f"{f + 1}.{schedule_of_lessons[f]}")


# ----|----

# Soft Uni course planing
#
#
# schedule_of_lessons = input().split(", ")
#
#
# command = input()
#
# while command != "course start":
#
#     instructions = command.split(":")
#
#     if instructions[0] == "Add":
#         if instructions[1] not in schedule_of_lessons:
#             schedule_of_lessons.append(instructions[1])
#     elif instructions[0] == "Insert":
#         if instructions[1] not in schedule_of_lessons:
#             schedule_of_lessons.insert(int(instructions[2]), instructions[1])
#     elif instructions[0] == "Remove":
#         for i in range(len(schedule_of_lessons)):
#             if schedule_of_lessons[i] == instructions[1]:
#                 schedule_of_lessons.pop(i)
#                 break
#     elif instructions[0] == "Swap":
#         if instructions[1] in schedule_of_lessons:
#             first_index = schedule_of_lessons.index(instructions[1])
#         else:
#             command = input()
#             continue
#
#         if instructions[2] in schedule_of_lessons:
#             second_index = schedule_of_lessons.index(instructions[2])
#         else:
#             command = input()
#             continue
#
#         first_index_group = []
#         second_index_group = []
#         if schedule_of_lessons[first_index + 1] == instructions[1] + "-Exercise":
#             first_index_group.append(schedule_of_lessons[first_index])
#             first_index_group.append(schedule_of_lessons[first_index + 1])
#         else:
#             first_index_group.append(schedule_of_lessons[first_index])
#
#         if second_index == len(schedule_of_lessons) - 1:
#             second_index_group.append(schedule_of_lessons[second_index])
#         elif schedule_of_lessons[second_index + 1] == instructions[2] + "-Exercise":
#             second_index_group.append(schedule_of_lessons[second_index])
#             second_index_group.append(schedule_of_lessons[second_index + 1])
#         else:
#             second_index_group.append(schedule_of_lessons[second_index])
#
#         schedule_of_lessons[first_index], schedule_of_lessons[second_index] = \
#             schedule_of_lessons[second_index], schedule_of_lessons[first_index]
#
#         if len(first_index_group) == 2 == len(second_index_group):
#             schedule_of_lessons[first_index + 1], schedule_of_lessons[second_index + 1] = \
#                 schedule_of_lessons[second_index + 1], schedule_of_lessons[first_index + 1]
#
#         if len(first_index_group) == 1 and len(second_index_group) == 2:
#             schedule_of_lessons.insert(first_index + 1, schedule_of_lessons.pop(second_index + 1))
#
#         if len(first_index_group) == 2 and len(second_index_group) == 1:
#             schedule_of_lessons.insert(second_index + 1, first_index_group[1])
#             schedule_of_lessons.pop(first_index + 1)
#
#     elif instructions[0] == "Exercise":
#
#         if schedule_of_lessons[-1] == instructions[1]:
#             schedule_of_lessons.append(instructions[1] + "-Exercise")
#             continue
#
#         if instructions[1] + "-Exercise" in schedule_of_lessons:
#             continue
#
#         for i in range(len(schedule_of_lessons)):
#             if schedule_of_lessons[i] == instructions[1]:
#                 schedule_of_lessons.insert(i + 1, instructions[1] + "-Exercise")
#         else:
#             schedule_of_lessons.append(instructions[1])
#             schedule_of_lessons.append(instructions[1] + "-Exercise")
#
#     command = input()
#
#
# for f in range(len(schedule_of_lessons)):
#     print(f"{f + 1}.{schedule_of_lessons[f]}")

# -----|-----

# Soft Uni course planing


schedule_of_lessons = input().split(", ")


command = input()

while command != "course start":

    instructions = command.split(":")

    if instructions[0] == "Add":
        if instructions[1] not in schedule_of_lessons:
            schedule_of_lessons.append(instructions[1])
    elif instructions[0] == "Insert":
        if instructions[1] not in schedule_of_lessons:
            schedule_of_lessons.insert(int(instructions[2]), instructions[1])
    elif instructions[0] == "Remove":
        remove_index = None
        if instructions[1] in schedule_of_lessons:
            remove_index = schedule_of_lessons.index(instructions[1])
        else:
            continue

        if remove_index == len(schedule_of_lessons) - 1:
            schedule_of_lessons.pop(remove_index)
        elif schedule_of_lessons[remove_index + 1] == instructions[1] + "-Exercise":
            schedule_of_lessons.pop(remove_index + 1)
            schedule_of_lessons.pop(remove_index)
        else:
            schedule_of_lessons.pop(remove_index)

    elif instructions[0] == "Swap":
        if instructions[1] in schedule_of_lessons:
            first_index = schedule_of_lessons.index(instructions[1])
        else:
            command = input()
            continue

        if instructions[2] in schedule_of_lessons:
            second_index = schedule_of_lessons.index(instructions[2])
        else:
            command = input()
            continue

        if second_index == len(schedule_of_lessons) - 1 and \
                "Exercise" in schedule_of_lessons[first_index + 1]:
            schedule_of_lessons[first_index], schedule_of_lessons[second_index] = \
                schedule_of_lessons[second_index], schedule_of_lessons[first_index]
            schedule_of_lessons.append(schedule_of_lessons.pop(first_index + 1))
            command = input()
            continue

        if second_index == len(schedule_of_lessons) - 1 and \
                "Exercise" not in schedule_of_lessons[first_index + 1]:
            schedule_of_lessons[first_index], schedule_of_lessons[second_index] = \
                schedule_of_lessons[second_index], schedule_of_lessons[first_index]
            command = input()
            continue

        if "Exercise" in schedule_of_lessons[first_index + 1] and "Exercise"\
                in schedule_of_lessons[second_index + 1]:
            schedule_of_lessons[first_index + 1], schedule_of_lessons[second_index + 1] = \
                schedule_of_lessons[second_index + 1], schedule_of_lessons[first_index]
            command = input()
            continue

        if "Exercise" in schedule_of_lessons[first_index + 1]:
            schedule_of_lessons[first_index], schedule_of_lessons[second_index] = \
                schedule_of_lessons[second_index], schedule_of_lessons[first_index]
            schedule_of_lessons.insert(second_index + 1, schedule_of_lessons.pop(first_index + 1))
            command = input()
            continue

        if "Exercise" in schedule_of_lessons[second_index + 1]:
            schedule_of_lessons[first_index], schedule_of_lessons[second_index] = \
                schedule_of_lessons[second_index], schedule_of_lessons[first_index]
            schedule_of_lessons.insert(first_index + 1, schedule_of_lessons.pop(second_index + 1))
            command = input()
            continue

    elif instructions[0] == "Exercise":

        if schedule_of_lessons[-1] == instructions[1]:
            schedule_of_lessons.append(instructions[1] + "-Exercise")
            continue

        for i in range(len(schedule_of_lessons)):
            if schedule_of_lessons[i] == instructions[1]:
                schedule_of_lessons.insert(i + 1, instructions[1] + "-Exercise")
                break
        else:
            schedule_of_lessons.append(instructions[1])
            schedule_of_lessons.append(instructions[1] + "-Exercise")

    command = input()


for f in range(len(schedule_of_lessons)):
    print(f"{f + 1}.{schedule_of_lessons[f]}")
