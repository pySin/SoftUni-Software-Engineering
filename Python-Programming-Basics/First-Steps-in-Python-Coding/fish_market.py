# Fish market

# ⦁	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
# ⦁	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
# ⦁	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
# ⦁	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
# ⦁	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]

MUSSELS_PER_KILO = 7.50

mackerel_per_kilo = float(input())
sprat_per_kilo = float(input())
bonito_kilos = float(input())
jack_mackerels_kilos = float(input())
mussels_kilos = int(input())

bonito_per_kilo = mackerel_per_kilo + (mackerel_per_kilo * 0.6)
jack_mackerels_per_kilo = sprat_per_kilo + (sprat_per_kilo * 0.80)

final_bill = (bonito_per_kilo * bonito_kilos) + (jack_mackerels_per_kilo * jack_mackerels_kilos) \
             + (mussels_kilos * MUSSELS_PER_KILO)

print(f"{final_bill:.2f}")
