# Which are in


sentence_1 = input().split(", ")
sentence_2 = input()

substrings_found = [word for word in sentence_1 if word in sentence_2]
print(substrings_found)
