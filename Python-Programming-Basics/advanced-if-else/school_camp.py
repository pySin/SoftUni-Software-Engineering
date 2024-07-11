# School Camp

# ⦁	Сезонът – текст - “Winter”, “Spring” или “Summer”;
# ⦁	Видът на групата – текст - “boys”, “girls” или “mixed”;
# ⦁	Брой на учениците – цяло число в интервала [1 … 10000];
# ⦁	Брой на нощувките – цяло число в интервала [1 … 100].

season = input()  # “Winter”, “Spring” или “Summer”
group_type = input()  # “boys”, “girls” или “mixed”
number_of_students = int(input())
number_of_nights = int(input())

sport = ""
accommodation_price = 0

if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        accommodation_price = (number_of_nights * number_of_students) * 9.60
        if group_type == "boys":
            sport = "Judo"
        elif group_type == "girls":
            sport = "Gymnastics"
    elif group_type == "mixed":
        accommodation_price = (number_of_nights * number_of_students) * 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        accommodation_price = (number_of_nights * number_of_students) * 7.20
        if group_type == "boys":
            sport = "Tennis"
        elif group_type == "girls":
            sport = "Athletics"
    elif group_type == "mixed":
        accommodation_price = (number_of_nights * number_of_students) * 9.50
        sport = "Cycling"

elif season == "Summer":
    if group_type == "boys" or group_type == "girls":
        accommodation_price = (number_of_nights * number_of_students) * 15
        if group_type == "boys":
            sport = "Football"
        elif group_type == "girls":
            sport = "Volleyball"

    elif group_type == "mixed":
        accommodation_price = (number_of_nights * number_of_students) * 20
        sport = "Swimming"

if number_of_students >= 50:
    accommodation_price *= 0.50
elif number_of_students >= 20:
    accommodation_price *= 0.85
elif number_of_students >= 10:
    accommodation_price *= 0.95


print(f"{sport} {accommodation_price :.2f} lv.")
