# Basketball expenses for a year.

annual_fee = int(input())

sneakers = annual_fee - (annual_fee * 0.40)  # %40 less than annual_fee
basketball_suit = sneakers - (sneakers * 0.20)  # %20 less than sneakers
ball = basketball_suit * 0.25  # ball = 1/4 of basketball_suit
accessories = ball * 0.20  # accessories = 1/5 of ball

yearly_basketball_expenses = annual_fee + sneakers + basketball_suit + ball + accessories
print(yearly_basketball_expenses)
print(yearly_basketball_expenses)
print(yearly_basketball_expenses)