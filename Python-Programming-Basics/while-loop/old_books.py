# Old books
NO_MORE_BOOKS_COMMAND = "No More Books"

book_looked_for = input()
number_of_searches = 0
is_found = False

current_command = input()
while current_command != NO_MORE_BOOKS_COMMAND:

    current_book = current_command
    if current_book == book_looked_for:
        is_found = True
        break

    number_of_searches += 1
    current_command = input()

if not is_found:
    print(f"The book you search is not here!")
    print(f"You checked {number_of_searches} books.")
else:
    print(f"You checked {number_of_searches} books and found it.")
