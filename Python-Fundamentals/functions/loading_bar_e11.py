# Loading Bar

def loading_bar(percentages):
    empty_bar = "[..........]"
    bar = empty_bar[0] + int(percentages / 10) * "%" + empty_bar[int(percentages / 10) + 1:]
    return percentages, f"{percentages}% {bar}"


percentage_number = int(input())

loading = loading_bar(percentage_number)
if loading[0] == 100:
    print("100% Complete!")
    print(loading[1][-12::1])
else:
    print(loading[1])
    print("Still loading...")
