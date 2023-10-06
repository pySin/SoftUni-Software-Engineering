# Stuttering Function

def stutter(word):
    phrase = ""
    for i in range(2):
        for j in range(2):
            phrase += word[j]
        phrase += "... "
    phrase += word
    phrase += "?"
    return phrase


word_example = input()
get_phrase = stutter(word_example)
print(get_phrase)
