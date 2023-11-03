# Social Distribution


wealth_levels = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

for i in range(len(wealth_levels)):
    if wealth_levels[i] < minimum_wealth:
        wealthiest_index = wealth_levels.index(max(wealth_levels))
        wealth_levels[wealthiest_index] -= (minimum_wealth - wealth_levels[i])
        wealth_levels[i] += minimum_wealth - wealth_levels[i]

if sum(wealth_levels) < len(wealth_levels) * minimum_wealth:
    print("No equal distribution possible")
else:
    print(wealth_levels)
