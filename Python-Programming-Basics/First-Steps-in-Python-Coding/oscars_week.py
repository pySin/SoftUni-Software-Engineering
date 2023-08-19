# Oscars Week

movie_name = input()
hall_type = input()
tickets_bought = int(input())

if movie_name == "A Star Is Born":
    if hall_type == "normal":
        income = tickets_bought * 7.50
        print(f"A Star Is Born -> {income:.2f} lv.")
    elif hall_type == "luxury":
        income = tickets_bought * 10.50
        print(f"A Star Is Born -> {income:.2f} lv.")
    elif hall_type == "ultra luxury":
        income = tickets_bought * 13.50
        print(f"A Star Is Born -> {income:.2f} lv.")

if movie_name == "Bohemian Rhapsody":
    if hall_type == "normal":
        income = tickets_bought * 7.35
        print(f"Bohemian Rhapsody -> {income:.2f} lv.")
    elif hall_type == "luxury":
        income = tickets_bought * 9.45
        print(f"Bohemian Rhapsody -> {income:.2f} lv.")
    elif hall_type == "ultra luxury":
        income = tickets_bought * 12.75
        print(f"Bohemian Rhapsody -> {income:.2f} lv.")

if movie_name == "Green Book":
    if hall_type == "normal":
        income = tickets_bought * 8.15
        print(f"Green Book -> {income:.2f} lv.")
    elif hall_type == "luxury":
        income = tickets_bought * 10.25
        print(f"Green Book -> {income:.2f} lv.")
    elif hall_type == "ultra luxury":
        income = tickets_bought * 13.25
        print(f"Green Book -> {income:.2f} lv.")

if movie_name == "The Favourite":
    if hall_type == "normal":
        income = tickets_bought * 8.75
        print(f"The Favourite -> {income:.2f} lv.")
    elif hall_type == "luxury":
        income = tickets_bought * 11.55
        print(f"The Favourite -> {income:.2f} lv.")
    elif hall_type == "ultra luxury":
        income = tickets_bought * 13.95
        print(f"The Favourite -> {income:.2f} lv.")
