# Students


def students(record):
    record = record.split(":")
    student_records[record[0]] = {record[1]: record[2]}


def add_records():
    command = input()

    while True:
        if ":" not in command:
            course_type = command.replace("_", " ")
            break
        else:
            students(command)
        command = input()
    return course_type


def course_find(target_course):
    for key, value in student_records.items():
        for nested_key, nested_value in value.items():
            if nested_value == target_course:
                print(f"{key} - {nested_key}")


if __name__ == "__main__":
    student_records = {}
    course = add_records()
    course_find(course)
