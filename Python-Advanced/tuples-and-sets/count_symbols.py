# Count Symbols


text = input()
text_set = sorted(set(text))


print(*[f"{x}: {text.count(x)} time/s" for x in text_set], sep="\n")
