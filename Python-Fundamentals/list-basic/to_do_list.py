# To do list

todo_list = []


def add_task(task):
    todo_list.append(task)
    print("Task added successfully!")


def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed successfully!")
    else:
        print("Write a task name")


def view_task():
    if todo_list:
        print("Tasks:")
        for task in todo_list:
            print(task)
    else:
        print("No tasks in my ToDo list")


while True:
    print("\n ----- ToDo List App -----")
    print("1. Add task")
    print("2. Remove task")
    print("3. View task")
    print("4. Exit")

    choice = input("Enter your choice(1-4)")

    if choice == "1":
        task_given = input("Enter a task:")
        add_task(task_given)
    elif choice == "2":
        task_given = input("Enter task to remove :")
        remove_task(task_given)
    elif choice == "3":
        view_task()
    elif choice == "4":
        print("Exiting the program!")
        break
    else:
        print("Invalid choice. Try again!")
