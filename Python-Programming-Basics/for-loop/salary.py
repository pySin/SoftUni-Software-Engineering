# Salary


# ⦁	Брой отворени табове в браузъра n - цяло число в интервала [1...10]
# ⦁	Заплата - число в интервала [500...1500]
# След това n – на брой пъти се чете име на уебсайт – текст

opened_tabs = int(input())
salary = int(input())

for _ in range(opened_tabs):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

    if salary <= 0:
        print(f"You have lost your salary.")
        break

    if _ == opened_tabs - 1:
        print(salary)
        break
