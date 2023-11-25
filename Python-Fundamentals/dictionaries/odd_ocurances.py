# Odd Occurrences


words = input().split()

occurrences = {}

for i in range(len(words)):
    if words[i].lower() in occurrences:
        occurrences[words[i].lower()] += 1
    else:
        occurrences[words[i].lower()] = 1

for prog_language in occurrences:
    if occurrences[prog_language] % 2 != 0:
        print(prog_language, end=" ")
