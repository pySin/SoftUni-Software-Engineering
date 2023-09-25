# Skip ovals from sentence

# Exercise 6: Skip ovals to print from the sentence ‘Python Logic For Kids’

sentence = "Python Logic For Kids"

for letter in sentence:
    if not letter == "o":
        print(letter, end="")
