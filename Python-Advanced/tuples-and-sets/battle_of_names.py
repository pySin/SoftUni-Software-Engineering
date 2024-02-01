# Battle of names


n = int(input())
even_set = set()
odd_set = set()

for i in range(1, n + 1):
    name = input()
    # name_ascii_score = 0
    # for letter in name:
    #     name_ascii_score += ord(letter)
    name_ascii_score = sum(ord(x) for x in name)

    name_score = name_ascii_score // i
    if name_score % 2 == 0:
        even_set.add(name_score)
    else:
        odd_set.add(name_score)


if sum(even_set) == sum(odd_set):
    print(*(even_set | odd_set), sep=", ")
elif sum(even_set) < sum(odd_set):
    print(*(odd_set - even_set), sep=", ")
elif sum(even_set) > sum(odd_set):
    print(*(even_set ^ odd_set), sep=", ")
