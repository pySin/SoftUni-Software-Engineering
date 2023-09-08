# Football League

# От конзолата се четат поредица от числа, всяко на отделен ред:
# Капацитетът на стадиона – цяло число в интервала [1 … 10000];
# Броят на всички фенове – цяло число в интервала [1 … 10000].
# За всеки един фен, на отделен ред се прочита:
# Секторът, на който се намира – текст – "A", "B", "V" и "G".

stadium_capacity = int(input())
fans_count = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for _ in range(fans_count):
    sector = input()

    if sector == "A":
        sector_a += 1
    if sector == "B":
        sector_b += 1
    if sector == "V":
        sector_v += 1
    if sector == "G":
        sector_g += 1

print(f"{(sector_a / fans_count) * 100 :.2f}%")
print(f"{(sector_b / fans_count) * 100 :.2f}%")
print(f"{(sector_v / fans_count) * 100 :.2f}%")
print(f"{(sector_g / fans_count) * 100 :.2f}%")
print(f"{(fans_count / stadium_capacity) * 100 :.2f}%")
