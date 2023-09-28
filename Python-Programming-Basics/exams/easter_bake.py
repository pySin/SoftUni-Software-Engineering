# Easter Bake

# Броят на козунаците – цяло число в интервала [1 ... 100]
# За всеки козунак се чете:
# Количество изразходвана захар (грамове) – цяло число в интервала [1 … 10000]
# Количество изразходвано брашно (грамове) – цяло число в интервала [1 … 10000]

sweet_breads = int(input())

whole_sugar_used = 0
whole_flour_used = 0

max_sugar_used = 0
max_flour_used = 0

x = 0
while x < sweet_breads:
    x += 1
    sugar_used = int(input())
    flour_used = int(input())

    if sugar_used > max_sugar_used:
        max_sugar_used = sugar_used

    if flour_used > max_flour_used:
        max_flour_used = flour_used

    whole_sugar_used += sugar_used
    whole_flour_used += flour_used

sugar_packs = 0
flour_packs = 0

if whole_sugar_used % 950 == 0:
    sugar_packs = whole_sugar_used // 950
else:
    sugar_packs = (whole_sugar_used // 950) + 1

if whole_flour_used % 750 == 0:
    flour_packs = whole_flour_used // 750
else:
    flour_packs = (whole_flour_used // 750) + 1

print(f"Sugar: {sugar_packs}")
print(f"Flour: {flour_packs}")
print(f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")
