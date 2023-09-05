# Back to the past


# Наследените пари – реално число в интервала [1.00 ... 1 000 000.00]
# Годината, до която трябва да живее (включително) – цяло число в интервала [1801 ... 1900]

inherited_money = float(input())
final_year = int(input())
ivan_years = 18

years_to_spend = final_year - 1800

for i in range(0, years_to_spend + 1):
    if i % 2 == 0:
        inherited_money -= 12000
    else:
        inherited_money -= 12000 + (50 * ivan_years)
    ivan_years += 1

if inherited_money < 0:
    print(f"He will need {abs(inherited_money) :.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {inherited_money :.2f} dollars left.")
