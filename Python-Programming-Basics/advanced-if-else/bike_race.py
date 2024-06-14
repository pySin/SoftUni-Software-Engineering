# Bike Race

# ⦁	Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
# ⦁	Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
# ⦁	Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"

juniors_count = int(input())
senior_count = int(input())
type_of_track = input()  # "trail", "cross-country", "downhill" или "road"

juniors_income = 0
seniors_income = 0
over_50_discount = "no"

if type_of_track == "trail":
    juniors_income = juniors_count * 5.50
    seniors_income = senior_count * 7
elif type_of_track == "cross-country":
    juniors_income = juniors_count * 8
    seniors_income = senior_count * 9.50
    if juniors_count + senior_count >= 50:
        over_50_discount = "yes"
elif type_of_track == "downhill":
    juniors_income = juniors_count * 12.25
    seniors_income = senior_count * 13.75
elif type_of_track == "road":
    juniors_income = juniors_count * 20
    seniors_income = senior_count * 21.50

profit = juniors_income + seniors_income

if over_50_discount == "yes":
    profit *= 0.75

profit *= 0.95
print(f"{profit :.2f}")
