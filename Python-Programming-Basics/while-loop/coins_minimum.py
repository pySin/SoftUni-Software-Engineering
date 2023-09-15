# Minimum coins amount

change_due = float(input())
to_stotinki = change_due * 100

lev_1 = 0
lev_2 = 0
coin_50 = 0
coin_20 = 0
coin_10 = 0
coin_5 = 0
coin_2 = 0
coin_1 = 0

while to_stotinki != 0:
    if to_stotinki >= 200:  # Can be done with if ... elif as well because it returns after True clause.
        lev_2 = to_stotinki // 200
        to_stotinki -= lev_2 * 200
        continue

    if to_stotinki >= 100:
        lev_1 = to_stotinki // 100
        to_stotinki -= lev_1 * 100
        continue

    if to_stotinki >= 50:
        coin_50 = to_stotinki // 50
        to_stotinki -= coin_50 * 50
        continue

    if to_stotinki >= 20:
        coin_20 = to_stotinki // 20
        to_stotinki -= coin_20 * 20
        continue

    if to_stotinki >= 10:
        coin_10 = to_stotinki // 10
        to_stotinki -= coin_10 * 10
        continue

    if to_stotinki >= 5:
        coin_5 = to_stotinki // 5
        to_stotinki -= coin_5 * 5
        continue

    if to_stotinki >= 2:
        coin_2 = to_stotinki // 2
        to_stotinki -= coin_2 * 2
        continue

    coin_1 = to_stotinki
    to_stotinki -= coin_1


all_coins = lev_2 + lev_1 + coin_50 + coin_20 + coin_10 + coin_5 + coin_2 + coin_1
print(int(all_coins))
