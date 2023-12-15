# Lesson
import re

# text = "The cost is 12.995867 lv"
# text_2 = "hi hiiii hiiih hiiii"
# pattern = r"\d+\.\d+"
# pattern_2 = "hi*"
#
#
# def regex_test(regex, string):
#     result = re.findall(regex, string)
#
#     if result:
#         print("Result found: ", result)
#     else:
#         print("No match found")
#
#
# regex_test(pattern_2, text_2)
# regex_test("\\bworld\\b", "Hello world")

# text = "The ball is red and big"
# pattern = "(red|blue) and (big|small)"
#
#
# def regex_test(regex, string):
#     result = re.findall(regex, string)
#
#     if result:
#         print("Result found: ", result)
#     else:
#         print("No match found")
#
#
# regex_test(pattern, text)


# text = "Python is fun."
# pattern = "^Python"
# pattern_2 = "fun\.$"
#
#
# def regex_test(regex, string):
#     result = re.findall(regex, string)
#
#     if result:
#         print("Result found: ", result)
#     else:
#         print("No match found")
#
#
# regex_test(pattern_2, text)

# text = "Python is an interpreted language."
# pattern = "[irn]"
#
#
# def regex_test(regex, string):
#     result = re.findall(regex, string)
#
#     if result:
#         print("Result found: ", result)
#         print(result.count("i"))
#     else:
#         print("No match found")
#
#
# regex_test(pattern, text)

# text = "Python is an interpreted language."
# pattern = "[a-n]"  # Alphabet Range
#
#
# def regex_test(regex, string):
#     result = re.findall(regex, string)
#
#     if result:
#         print("Result found: ", result)
#         print(result.count("i"))
#     else:
#         print("No match found")


# regex_test(pattern, text)

# text = "Python is an interpreted language."
# pattern = "[^a-n]"  # Alphabet Range
#
#
# def regex_test(regex, string):
#     result = re.findall(regex, string)
#
#     if result:
#         print("Result found: ", result)
#         print(result.count("i"))
#     else:
#         print("No match found")
#
#
# regex_test(pattern, text)


# text = "Python is an interpreted language. 1234"
# pattern = "[a-zA-Z0-9]"  #
#
#
# def regex_test(regex, string):
#     result = re.findall(regex, string)
#
#     if result:
#         print("Result found: ", result)
#     else:
#         print("No match found")
#
#
# regex_test(pattern, text)

# -- Search method

# text = "Once upon a time"
# pattern = "e"
#
# matching = re.search(pattern, text)
# print(matching)
# print(matching.start())


# -- re.search()

# string = "The quick brown fox jumps over the lazy dog. Python is fun. Programming is fun!"
#
# match = re.search(r'\bp\w*', string, re.IGNORECASE)
#
# if match:
#     print(f"The first word that starts with p is: {match.group()}")
# else:
#     print("No word starting with \"p\"")


# -- split() method

# string = "The quick brown fox jumps over the lazy dog. Python is fun. Programming is fun!"
# pattern = "\s"
#
# string_x = re.split(pattern, string)
# print(string_x)


# -- re.sub() method
# string = "There are 3 dogs and 4 cats"
# result = re.sub('\d', "number", string)
# result_n = re.subn('\d', "number", string)  # Shows how many substitutions there were in tuple.
#
# print(result)


# -- re.MULTILINE(re.M) flag
# text = '''start one
# start_two
# '''
# print(re.findall("^start", text))
#
# print(re.findall("^start", text, re.M))

# -- multiline patterns

pattern = """
    ^
    (19|20)\d\d  # start of string
    -
    (0[1-9]|1[012])  # Year
    -
    (0[1-9]|[012][0-9]|3[01])  # Day
    $
          """

text = "2022-07-12"
print(re.fullmatch(pattern, text, re.X))
for item in re.fullmatch(pattern, text, re.X).group():
    print(item)
