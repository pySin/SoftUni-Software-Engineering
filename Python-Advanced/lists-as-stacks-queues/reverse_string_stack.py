# Reverse string using stacks

sentence = list(input())

# for i in range(len(sentence)):
#     print(sentence.pop(), end="")

reversed_sentence = ""

for i in range(len(sentence)):
    reversed_sentence += sentence.pop()

print(reversed_sentence)
