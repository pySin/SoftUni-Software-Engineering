# Coffee Machine

# Първи ред - напитка - текст с възможности"Espresso", "Cappuccino" или "Tea"
# Втори ред - захар - текст  с възможности "Without", "Normal" или "Extra"
# Трети ред - брой напитки - цяло число в интервала [1… 50]

hot_drink = input()
sugar_amount = input()
number_of_drinks = int(input())

drinks_bill = 0

if hot_drink == "Espresso":
    if sugar_amount == "Without":
        if number_of_drinks >= 5:
            drinks_bill = ((number_of_drinks * 0.90) * 0.65) * 0.75
            if drinks_bill > 15:
                drinks_bill *= 0.80
        else:
            drinks_bill = (number_of_drinks * 0.90) * 0.65
            if drinks_bill > 15:
                drinks_bill *= 0.80
    elif sugar_amount == "Normal":
        if number_of_drinks >= 5:
            drinks_bill = ((number_of_drinks * 0.90) * 0.65) * 0.75
            if drinks_bill > 15:
                drinks_bill *= 0.80
        else:
            drinks_bill = number_of_drinks * 1
            if drinks_bill > 15:
                drinks_bill *= 0.80
    else:
        if number_of_drinks >= 5:
            drinks_bill = ((number_of_drinks * 1.20) * 0.65) * 0.75
            if drinks_bill > 15:
                drinks_bill *= 0.80
        else:
            drinks_bill = number_of_drinks * 1.20
            if drinks_bill > 15:
                drinks_bill *= 0.80

if hot_drink == "Cappuccino":
    if sugar_amount == "Without":
        drinks_bill = (number_of_drinks * 1) * 0.65
        if drinks_bill > 15:
            drinks_bill *= 0.80
    elif sugar_amount == "Normal":
        drinks_bill = number_of_drinks * 1.20
        if drinks_bill > 15:
            drinks_bill *= 0.80
    else:
        drinks_bill = number_of_drinks * 1.60
        if drinks_bill > 15:
            drinks_bill *= 0.80

if hot_drink == "Tea":
    if sugar_amount == "Without":
        drinks_bill = (number_of_drinks * 0.50) * 0.65
        if drinks_bill > 15:
            drinks_bill *= 0.80
    elif sugar_amount == "Normal":
        drinks_bill = number_of_drinks * 0.60
        if drinks_bill > 15:
            drinks_bill *= 0.80
    else:
        drinks_bill = number_of_drinks * 0.70
        if drinks_bill > 15:
            drinks_bill *= 0.80

print(f"You bought {number_of_drinks} cups of {hot_drink} for {drinks_bill :.2f} lv.")
