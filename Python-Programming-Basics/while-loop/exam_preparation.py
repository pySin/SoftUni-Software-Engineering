# Exam Preparation

# ⦁	На първи ред - брой незадоволителни оценки - цяло число;
# ⦁	След това многократно се четат по два реда:
# ⦁	Име на задача – текст;
# ⦁	Оценка - цяло число в интервала [2…6]

low_marks_count = int(input())
initial_low_marks = low_marks_count
marks_sum = 0
marks_count = 0
is_enough_tasks = False
is_low_marks_reached = False
current_task_name = None

task_name = input()
while not is_enough_tasks:

    if task_name == "Enough":
        is_enough_tasks = True
        continue

    current_task_name = task_name
    current_mark = int(input())

    if current_mark <= 4:
        low_marks_count -= 1
        if low_marks_count == 0:
            is_low_marks_reached = True
            break

    marks_sum += current_mark
    marks_count += 1
    task_name = input()

if is_enough_tasks:
    print(f"Average score: {marks_sum / marks_count :.2f}")
    print(f"Number of problems: {marks_count}")
    print(f"Last problem: {current_task_name}")
elif is_low_marks_reached:
    print(f"You need a break, {initial_low_marks} poor grades.")
