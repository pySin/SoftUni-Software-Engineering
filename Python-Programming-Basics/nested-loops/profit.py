# Profit

# ⦁	Брой монети по 1лв. - цяло положително число;
# ⦁	Брой монети по 2лв. - цяло положително число;
# ⦁	Брой банкноти по 5лв. - цяло положително число;
# ⦁	Сума - цяло положително число в интервала [1…1000]

coins_1_lev = int(input())
coins_2_lev = int(input())
banknote_5_lev = int(input())
full_amount = int(input())

for coin_1 in range(coins_1_lev + 1):
    for coin_2 in range(coins_2_lev + 1):
        for banknote_5 in range(banknote_5_lev + 1):
            current_sum = (coin_1 * 1) + (coin_2 * 2) + (banknote_5 * 5)
            if current_sum == full_amount:
                print(f"{coin_1} * 1 lv. + {coin_2} * 2 lv. "
                      f"+ {banknote_5} * 5 lv. = {full_amount} lv.")
