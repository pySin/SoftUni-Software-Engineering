# Word Filter


# text_of_words = filter(lambda x: len(x) % 2 == 0, input().split(" "))
text_of_words = [word for word in input().split(" ") if len(word) % 2 == 0]
[print(word) for word in text_of_words]
