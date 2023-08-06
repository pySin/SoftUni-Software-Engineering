# Cinema tickets

# Входът е поредица от цели числа и текст:
# На първия ред до получаване на командата "Finish" - име на филма – текст
# На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
# Типа на закупения билет - текст ("student", "standard", "kid")

movie_name = ""
total_tickets = 0
standard_tickets = 0.00
student_tickets = 0.00
kids_tickets = 0.00

while movie_name != "Finish":
    movie_name = input()
    if movie_name == "Finish":
        break
    available_seats = int(input())
    initial_available_seats = available_seats
    type_of_ticket = ""
    tickets_sold = 0
    while available_seats > 0:
        type_of_ticket = input()
        if type_of_ticket == "End":
            break
        elif type_of_ticket == "standard":
            standard_tickets += 1
        elif type_of_ticket == "student":
            student_tickets += 1
        elif type_of_ticket == "kid":
            kids_tickets += 1
        available_seats -= 1
        tickets_sold += 1
        total_tickets += 1

    percent_sold = (tickets_sold / initial_available_seats) * 100
    print(f"{movie_name} - {percent_sold:.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{((student_tickets / total_tickets) * 100):.2f}% student tickets.")
print(f"{((standard_tickets / total_tickets) * 100):.2f}% standard tickets.")
print(f"{((kids_tickets / total_tickets) * 100):.2f}% kids tickets.")
