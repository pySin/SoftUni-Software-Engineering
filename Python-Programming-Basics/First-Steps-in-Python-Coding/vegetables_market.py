# Vegetables Market

vegetables_price_per_kilo = float(input())
fruits_price_per_kilo = float(input())

kilos_of_vegetables = int(input())
kilos_of_fruit = int(input())

bgn_to_eur_rate = 1.94

income = ((vegetables_price_per_kilo * kilos_of_vegetables)
          + (fruits_price_per_kilo * kilos_of_fruit)) / bgn_to_eur_rate

print(f"{income:.2f}")
