# Sum Of A Beach

words = ["Sand", "Water", "Fish", "Sun"]
current_word = input()

appearances = 0

for i in range(len(words)):
    appearances += current_word.lower().count(words[i].lower())

print(appearances)
