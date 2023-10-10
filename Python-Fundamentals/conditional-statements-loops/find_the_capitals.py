# Find the capitals


word = input()
capital_indices = []

for i in range(len(word)):
    if word[i].isupper():
        capital_indices.append(i)

print(capital_indices)
