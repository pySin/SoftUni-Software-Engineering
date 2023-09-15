# Sum of Resistance in Series Circuits

lst = [0.5, 0.5]


def series_resistance(lst):
    resistance_sum = 0
    series = 0
    while series < len(lst):
        resistance_sum += lst[series]
        series += 1

    if resistance_sum > 1:
        print(f"{resistance_sum} ohms")
    else:
        print(f"{resistance_sum} ohm")


series_resistance(lst)
