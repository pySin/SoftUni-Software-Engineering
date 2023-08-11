# Godzilla versus Cong Budget

movie_budget = float(input())
supernumerary = int(input())
single_supernumerary_clothing = float(input())

movie_decor_bill = movie_budget * 0.10
supernumerary_clothing_bill = 0

if supernumerary > 150:
    supernumerary_clothing_bill = (supernumerary * single_supernumerary_clothing) \
                                   - ((supernumerary * single_supernumerary_clothing) * 0.10)
else:
    supernumerary_clothing_bill = supernumerary * single_supernumerary_clothing

full_bill = movie_decor_bill + supernumerary_clothing_bill
money_left = movie_budget - full_bill

if money_left >= 0:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
elif money_left < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(money_left):.2f} leva more.")
