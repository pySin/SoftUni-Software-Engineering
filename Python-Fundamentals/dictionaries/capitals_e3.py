# Capitals


def capitals(countries, this_capitals):
    countries = countries.split(", ")
    this_capitals = this_capitals.split(", ")

    country_capitals = {countries[index]: this_capitals[index] for index in range(len(countries))}
    return country_capitals


get_countries = input()
get_capitals = input()

for current_country, current_capital in capitals(get_countries, get_capitals).items():
    print(f"{current_country} -> {current_capital}")
