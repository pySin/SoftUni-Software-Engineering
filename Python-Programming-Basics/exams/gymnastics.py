# Gymnastics

# Първи ред – държава – текст ("Russia", "Bulgaria" или "Italy")
# Втори ред – уред - текст ("ribbon", "hoop" или "rope")

country = input()  # "Russia", "Bulgaria" или "Italy"
tool = input()  # "ribbon", "hoop" или "rope"

difficulty = 0
performance = 0


if tool == "ribbon":
    if country == "Russia":
        difficulty = 9.100
        performance = 9.400
    elif country == "Bulgaria":
        difficulty = 9.600
        performance = 9.400
    elif country == "Italy":
        difficulty = 9.200
        performance = 9.500
if tool == "hoop":
    if country == "Russia":
        difficulty = 9.300
        performance = 9.800
    elif country == "Bulgaria":
        difficulty = 9.550
        performance = 9.750
    elif country == "Italy":
        difficulty = 9.450
        performance = 9.350
if tool == "rope":
    if country == "Russia":
        difficulty = 9.600
        performance = 9.000
    elif country == "Bulgaria":
        difficulty = 9.500
        performance = 9.400
    elif country == "Italy":
        difficulty = 9.700
        performance = 9.150

print(f"The team of {country} get {difficulty + performance :.3f} on {tool}.")
print(f"{100 - (((difficulty + performance) / 20) * 100) :.2f}%")
