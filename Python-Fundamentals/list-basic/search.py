# Search word

number_of_phrases = int(input())
keyword = input()

all_phrases = []

for i in range(number_of_phrases):
    current_phrase = input()
    all_phrases.append(current_phrase)

phrases_with_keyword = []

for phrase_index in range(number_of_phrases):
    if keyword in all_phrases[phrase_index]:
        phrases_with_keyword.append(all_phrases[phrase_index])

print(all_phrases)
print(phrases_with_keyword)
