# Painting Eggs

# Първи ред – размер на яйцата – текст с възможности "Large", "Medium" или "Small"
# Втори ред – цвят на яйцата – текст  с възможности "Red", "Green" или "Yellow"
# Трети ред – брой партиди – цяло число в интервала [1… 350]

eggs_size = input()
eggs_color = input()
packages = int(input())

income = 0

if eggs_size == "Large":
    if eggs_color == "Red":
        income = packages * 16
    if eggs_color == "Green":
        income = packages * 12
    if eggs_color == "Yellow":
        income = packages * 9
if eggs_size == "Medium":
    if eggs_color == "Red":
        income = packages * 13
    if eggs_color == "Green":
        income = packages * 9
    if eggs_color == "Yellow":
        income = packages * 7
if eggs_size == "Small":
    if eggs_color == "Red":
        income = packages * 9
    if eggs_color == "Green":
        income = packages * 8
    if eggs_color == "Yellow":
        income = packages * 5

income *= 0.65
print(f"{income :.2f} leva.")
