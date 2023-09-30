# The most Powerful Word
from math import floor


word = ""
top_word = ""
top_score = 0

while word != "End of words":

    word = input()
    if word == "End of words":
        break
    current_score = 0

    x = 0
    y = ""
    for letter in word:
        x += 1
        if x == 1:
            y = letter
        current_score += ord(letter)

    if y in ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y",]:
        current_score = current_score * len(word)
    else:
        current_score = floor(current_score / len(word))

    if current_score >= top_score:
        top_word = word
        top_score = current_score

print(f"The most powerful word is {top_word} - {top_score}")
