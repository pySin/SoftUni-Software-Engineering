# Enrolment


def gather_credits(credits_needed: int, *args):
    if not args:
        return None
    collected_credits = 0
    courses_taken = []
    for course_name, current_credits in args:
        if course_name in courses_taken:
            continue
        courses_taken.append(course_name)
        collected_credits += int(current_credits)
        if collected_credits >= credits_needed:
            break

    display_message = ""
    courses_taken = sorted(courses_taken)
    if collected_credits >= credits_needed:
        display_message += f"Enrollment finished! Maximum credits: {collected_credits}.\n"
        display_message += f"Courses: {', '.join(courses_taken)}"
    else:
        credits_remain = credits_needed - collected_credits
        display_message += f"You need to enroll in more courses! You have to gather {credits_remain} credits more."
    return display_message


print(gather_credits(
    80
))
