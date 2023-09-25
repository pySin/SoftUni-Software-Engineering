# Wedding Seats

# ⦁	Последния сектор от секторите - символ (B-Z)
# ⦁	Броят на редовете в първия сектор - цяло число (1-100)
# ⦁	Броят на местата на нечетен ред - цяло число (1-24)

last_sector = input()
sector_rows = int(input())
odd_row_seats = int(input())

alphabet_small = "abcdefghijklmnopqrstuvwxyz"
alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
seats = 0
big_letter_count = 0

while True:

    for row in range(1, sector_rows + 1):
        if row % 2 != 0:
            for seat in range(odd_row_seats):
                seats += 1
                print(f"{alphabet_big[big_letter_count]}{row}{alphabet_small[seat]}")
        else:
            for seat in range(odd_row_seats + 2):
                seats += 1
                print(f"{alphabet_big[big_letter_count]}{row}{alphabet_small[seat]}")
    if alphabet_big[big_letter_count] == last_sector:
        break
    big_letter_count += 1
    sector_rows += 1
print(seats)
