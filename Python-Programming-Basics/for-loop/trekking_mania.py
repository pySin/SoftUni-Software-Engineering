# Trekking mania

# ⦁	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# ⦁	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]

groups_count = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
people_count = 0

for _ in range(groups_count):
    people_per_group = int(input())
    people_count += people_per_group

    if people_per_group <= 5:
        musala += people_per_group
    elif 6 <= people_per_group <= 12:
        monblan += people_per_group
    elif 13 <= people_per_group <= 25:
        kilimanjaro += people_per_group
    elif 26 <= people_per_group <= 40:
        k2 += people_per_group
    elif people_per_group > 40:
        everest += people_per_group


print(f"{(musala / people_count) * 100 :.2f}%")
print(f"{(monblan / people_count) * 100 :.2f}%")
print(f"{(kilimanjaro / people_count) * 100 :.2f}%")
print(f"{(k2 / people_count) * 100 :.2f}%")
print(f"{(everest / people_count) * 100 :.2f}%")
