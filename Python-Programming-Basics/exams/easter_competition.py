# Easter Competiton

# Първоначално от конзолата се прочита броя на козунаците – цяло число в интервала [1… 100]
# След това за всеки козунак се прочита:
# Името на пекаря, който е направил козунака – текст
# До получаване на командата "Stop" се прочита
# оценка за козунак от един човек  – цяло число в интервала [1... 10]

sweet_breads_amount = int(input())
top_baker = ""
max_points = 0

x = 0
while x < sweet_breads_amount:
    x += 1
    baker = input()

    sweet_bread_result = 0
    while True:

        sweet_bread_evaluation = input()
        if sweet_bread_evaluation == "Stop":
            print(f"{baker} has {sweet_bread_result} points.")
            if sweet_bread_result > max_points:
                print(f"{baker} is the new number 1!")
            break
        else:
            sweet_bread_result += int(sweet_bread_evaluation)

    if sweet_bread_result > max_points:
        max_points = sweet_bread_result
        top_baker = baker

print(f"{top_baker} won competition with {max_points} points!")
