# Add Bags

# Цената на багаж над 20кг - реално число в диапазона [10.0…80.0]
# Килограми на багажа – реално число в диапазона [1.0…32.0]
# Дни до пътуването – цяло число в диапазона [1…60]
# Брой багажи – цяло число в диапазона [1…10]

luggage_price_over_20_kg = float(input())
luggage_weight = float(input())
days_to_trip = int(input())
number_of_luggage = int(input())

luggage_price = 0

if luggage_weight < 10:
    luggage_price += (luggage_price_over_20_kg * 0.20) * number_of_luggage
elif 10 <= luggage_weight <= 20:
    luggage_price += (luggage_price_over_20_kg * 0.50) * number_of_luggage
elif luggage_weight > 20:
    luggage_price += luggage_price_over_20_kg * number_of_luggage

if days_to_trip > 30:
    luggage_price *= 1.10
elif 7 <= days_to_trip <= 30:
    luggage_price *= 1.15
else:
    luggage_price *= 1.40

print(f"The total price of bags is: {luggage_price:.2f} lv.")
