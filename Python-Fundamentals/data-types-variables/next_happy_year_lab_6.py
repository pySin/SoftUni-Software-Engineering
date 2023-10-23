# Next Happy Year

current_year = int(input())
is_happy_year = False
while True:

    current_year += 1

    string_year = str(current_year)
    # print(len(string_year))
    for i in range(len(string_year)):
        if string_year.count(string_year[i]) > 1:
            break
        elif i + 1 == len(string_year):
            is_happy_year = True

    if is_happy_year:
        break
    # current_year += 1

print(current_year)
