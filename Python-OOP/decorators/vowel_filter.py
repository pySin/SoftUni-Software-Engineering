# Vowel Filter


def vowel_filter(function):
    def wrapper():
        vowels = [v for v in function() if v in "aeoui"]
        return vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
