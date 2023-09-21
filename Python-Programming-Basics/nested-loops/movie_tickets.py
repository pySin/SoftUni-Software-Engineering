# Movie Tickets

current_movie = input()

all_tickets = 0
student_tickets = 0
normal_tickets = 0
children_tickets = 0
while current_movie != "Finish":

    available_spaces = int(input())
    seats_filled = 0
    current_visitor = input()
    while current_visitor != "End":
        seats_filled += 1
        all_tickets += 1
        if current_visitor == "student":
            student_tickets += 1
        elif current_visitor == "standard":
            normal_tickets += 1
        elif current_visitor == "kid":
            children_tickets += 1

        if seats_filled >= available_spaces:
            break
        current_visitor = input()

    print(f"{current_movie} - {(seats_filled / available_spaces) * 100:.2f}% full.")

    current_movie = input()


print(f"Total tickets: {all_tickets}")
print(f"{(student_tickets / all_tickets) * 100:.2f}% student tickets.")
print(f"{(normal_tickets / all_tickets) * 100:.2f}% standard tickets.")
print(f"{(children_tickets / all_tickets) * 100:.2f}% kids tickets.")
