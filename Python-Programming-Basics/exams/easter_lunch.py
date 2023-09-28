# Easter Lunch

# Брой козунаци - цяло число в интервала [0 … 99]
# Брой кори с яйца - цяло число в интервала [0 … 99]
# Килограми курабии - цяло число в интервала [0 … 99]

sweet_bread = int(input())
egg_packs = int(input())
cookie = int(input())

bill = (sweet_bread * 3.20) + (egg_packs * 4.35) + (cookie * 5.40) + ((egg_packs * 12) * 0.15)

print(f"{bill :.2f}")
