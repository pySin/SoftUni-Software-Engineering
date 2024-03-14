# Flower Finder
from collections import deque


vowels = deque(input().split())
consonants = input().split()

words_to_find = ["rose", "tulip", "lotus", "daffodil"]
letters_collected = []
word_found = None

is_word_found = False
while vowels and consonants:
    first_vowel = vowels.popleft()
    last_consonant = consonants.pop()

    letters_collected.append(first_vowel)
    letters_collected.append(last_consonant)

    for word in words_to_find:
        for i in range(len(word)):
            if word[i] not in letters_collected:
                break
            else:
                if i == len(word) - 1:
                    word_found = word
                    is_word_found = True
                    break
        if is_word_found:
            break
    if is_word_found:
        break

if word_found:
    print(f"Word found: {word_found}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
