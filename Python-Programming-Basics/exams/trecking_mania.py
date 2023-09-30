# Trecking Mania

# На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]

groups_amount = int(input())

musala_people = 0
montblanc_people = 0
kilimanjaro_people = 0
k2_people = 0
everest_people = 0


for _ in range(groups_amount):
    group_size = int(input())

    if group_size < 6:
        musala_people += group_size
    elif 6 <= group_size <= 12:
        montblanc_people += group_size
    if 12 < group_size <= 25:
        kilimanjaro_people += group_size
    if 25 < group_size <= 40:
        k2_people += group_size
    if group_size > 40:
        everest_people += group_size

all_people = montblanc_people + musala_people + kilimanjaro_people + k2_people + everest_people

print(f"{(musala_people / all_people) * 100 :.2f}%")
print(f"{(montblanc_people / all_people) * 100 :.2f}%")
print(f"{(kilimanjaro_people / all_people) * 100 :.2f}%")
print(f"{(k2_people / all_people) * 100 :.2f}%")
print(f"{(everest_people / all_people) * 100 :.2f}%")
