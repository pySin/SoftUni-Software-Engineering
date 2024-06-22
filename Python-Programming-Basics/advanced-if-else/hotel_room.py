# hotel Room

# ⦁	На първия ред е месецът - May, June, July, August, June или October;
# ⦁	На втория ред е броят на нощувките - цяло число.

month = input()  # May, June, July, August, September или October
number_of_accommodations = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < number_of_accommodations <= 14:
        studio_price *= 0.95
    elif number_of_accommodations > 14:
        studio_price *= 0.70

elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if number_of_accommodations > 14:
        studio_price *= 0.80
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

if number_of_accommodations > 14:
    apartment_price *= 0.90

studio_bill = studio_price * number_of_accommodations
apartment_bill = apartment_price * number_of_accommodations

print(f"Apartment: {apartment_bill :.2f} lv.")
print(f"Studio: {studio_bill :.2f} lv.")
