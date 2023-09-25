# Secret Doors Lock

# ⦁	Горната граница на стотиците - цяло число в диапазона (1-9)
# ⦁	Горната граница на десетиците - цяло число в диапазона (1-9)
# ⦁	Горната граница на единиците - цяло число в диапазона (1-9)

third_digit = int(input())
second_digit = int(input())
first_digit = int(input())

for i in range(1, third_digit + 1):
    for j in range(2, second_digit + 1):
        for h in range(1, first_digit + 1):
            if i % 2 == 0 and h % 2 == 0:
                if j == 2 or j == 3 or j == 5 or j == 7:
                    print(f"{i} {j} {h}")
