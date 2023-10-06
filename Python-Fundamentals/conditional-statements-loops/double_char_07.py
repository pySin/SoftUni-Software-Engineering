# Double Char

phrase = input()

while phrase != "End":

    if phrase == "SoftUni":
        phrase = input()
        continue

    double_phrase = ""
    for char in range(len(phrase)):
        double_phrase += phrase[char] * 2

    print(double_phrase)
    phrase = input()

