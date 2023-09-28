# Easter eggs

# Броят на боядисаните яйца – цяло число в интервала [1 ... 100]
# За всяко яйце се чете:
# Цветът на яйцето – текст с възможности: "red", "orange", "blue", "green"

eggs_amount = int(input())

red = 0
orange = 0
blue = 0
green = 0

x = 0
while x < eggs_amount:
    x += 1
    egg_color = input()

    if egg_color == "red":
        red += 1
    if egg_color == "orange":
        orange += 1
    if egg_color == "blue":
        blue += 1
    if egg_color == "green":
        green += 1

max_eggs = 0
max_eggs_color = ""

if red > orange and  red > blue and red > green:
    max_eggs = red
    max_eggs_color = "red"
elif orange > red and orange > blue and orange > green:
    max_eggs = orange
    max_eggs_color = "orange"
elif blue > red and blue > orange and blue > green:
    max_eggs = blue
    max_eggs_color = "blue"
else:
    max_eggs = green
    max_eggs_color = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_eggs_color}")
