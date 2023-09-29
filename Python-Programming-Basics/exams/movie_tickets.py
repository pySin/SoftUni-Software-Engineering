# Movie Tickets

# a1 – цяло число в интервала [65… 89]
# a2 – цяло число в интервала [66… 91]
# n – цяло число в интервала [1… 10]

a1 = int(input())
a2 = int(input())
n = int(input())

symbol_1 = ""
symbol_2 = 0
symbol_3 = 0
symbol_4 = 0


for i in range(a1, a2):
    symbol_1 = chr(i)
    for num_1 in range(1, n):
        symbol_2 = num_1
        for num_2 in range(1, int(n / 2)):
            symbol_3 = num_2
            symbol_4 = i
            three_symbols_sum = symbol_2 + symbol_3 + symbol_4
            if i % 2 != 0 and three_symbols_sum % 2 != 0:
                print(f"{symbol_1}-{symbol_2}{symbol_3}{symbol_4}")
