# Pol Entrance
from math import ceil, floor

SHAISE_LONGUE_RATIO = 0.75

# Първи ред – брой на хората. Цяло число в интервала [1…100]
# Втори ред – такса вход. Реално число в интервала [0.00…50.00]
# Трети ред – цена един за шезлонг. Реално число в интервала [0.00…50.00]
# Четвърти ред – цена за един чадър. Реално число в интервала [0.00...50.00]

amount_of_people = int(input())
entrance_fee = float(input())
chaise_longue_fee = float(input())
umbrella_fee = float(input())

umbrellas_bill = ceil(amount_of_people / 2) * umbrella_fee
chaise_longue_bill = ceil(amount_of_people * SHAISE_LONGUE_RATIO) * chaise_longue_fee

pool_bill = (amount_of_people * entrance_fee) + umbrellas_bill + chaise_longue_bill
print(f"{pool_bill :.2f} lv.")
