# # Recursion Palindrome
#
#
# def palindrome(word, index):
#     if index == len(word) - 1:
#         return word[index]
#     result = palindrome(word, index + 1) + word[index]
#     # print(result)
#     if index == 0:
#         if result == word:
#             return f"{word} is a palindrome"
#         else:
#             return f"{word} is not a palindrome"
#     return result
#
#
# print(palindrome("abcba", 0))


# Atanas Atanasov's solution

def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] != word[-1 - index]:  # TODO finish it
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
print()
print(palindrome("peter", 0))
