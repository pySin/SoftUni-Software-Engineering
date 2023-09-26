# Club

# На първия ред – желаната печалба на клуба - реално число в интервала [1.00... 15000.00]
# Поредица от два реда до получаване на командата "Party!" или до достигане на желаната печалба:
# Име на коктейла – текст
# Брой на коктейлите за поръчката – цяло число в интервала [1… 50]


profit_desired = float(input())

income = 0

while income < profit_desired:
    cocktail_name = input()
    if cocktail_name == "Party!":
        print(f"We need {profit_desired - income :.2f} leva more.")
        break

    number_of_cocktails = int(input())



    current_bill = len(cocktail_name) * number_of_cocktails
    if current_bill % 2 != 0:
        current_bill *= 0.75
    income += current_bill

if income >= profit_desired:
    print("Target acquired.")
print(f"Club income - {income :.2f} leva.")
