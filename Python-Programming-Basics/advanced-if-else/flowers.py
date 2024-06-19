# Flowers

# ⦁	На първия ред е броят на закупените хризантеми – цяло число в интервала [0 ... 200]
# ⦁	На втория ред е броят на закупените рози – цяло число в интервала [0 ... 200]
# ⦁	На третия ред е броят на закупените лалета – цяло число в интервала [0 ... 200]
# ⦁	На четвъртия ред е посочен сезона – [Spring, Summer, Аutumn, Winter]
# ⦁	На петия ред е посочено дали денят е празник – [Y – да / N - не]

chrysanthemum_count = int(input())
rose_count = int(input())
tulip_count = int(input())
season = input()
bank_holiday = input()

chrysanthemum_bill = 0
tulip_bill = 0
rose_bill = 0

if season == "Spring" or season == "Summer":
    chrysanthemum_bill = chrysanthemum_count * 2
    tulip_bill = tulip_count * 2.50
    rose_bill = rose_count * 4.10
elif season == "Autumn" or season == "Winter":
    chrysanthemum_bill = chrysanthemum_count * 3.75
    tulip_bill = tulip_count * 4.15
    rose_bill = rose_count * 4.50

whole_bill = chrysanthemum_bill + rose_bill + tulip_bill
if bank_holiday == "Y":
    whole_bill *= 1.15

if tulip_count > 7 and season == "Spring":
    whole_bill *= 0.95

if rose_count >= 10 and season == "Winter":
    whole_bill *= 0.90

if chrysanthemum_count + tulip_count + rose_count > 20:
    whole_bill *= 0.80
whole_bill += 2  # Florist

print(f"{whole_bill :.2f}")
