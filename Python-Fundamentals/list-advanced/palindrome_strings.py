# Palindrome Strings

words = input()
main_palindrome = input()


def palindrome_find(words_row, target_palindrome):
    words_divide = words_row.split(" ")
    palindromes = [word for word in words_divide if word == word[::-1]]
    main_palindrome_count = palindromes.count(target_palindrome)
    return palindromes, main_palindrome_count


result = palindrome_find(words, main_palindrome)
print(result[0])
print(f"Found palindrome {result[1]} times")
