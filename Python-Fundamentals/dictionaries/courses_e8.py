# Courses


def courses():

    courses_list = {}
    command = input()

    while command != "end":

        current_student = command.split(" : ")
        course = current_student[0]
        student = current_student[1]
        if course not in courses_list.keys():
            courses_list[course] = [student]
        else:
            courses_list[course].append(student)
        command = input()

    return courses_list


if __name__ == "__main__":
    for prog_course, it_student in courses().items():
        print(f"{prog_course}: {len(it_student)}")
        for single_student in it_student:
            print(f"-- {single_student}")
