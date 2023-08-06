# Celsius to Fahrenheit
# °F = (°C × 1.8) + 32
CELSIUS_TO_FAHRENHEIT_FORMULA_RATIO = 1.8

celsius = float(input())

fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FORMULA_RATIO) + 32
print(f"{fahrenheit:.2f}")
