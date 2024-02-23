# Concatenate


def concatenate(*args, **kwargs):
    concatenated = "".join(args)
    for key, value in kwargs.items():
        if key in concatenated:
            concatenated = concatenated.replace(key, value)
    return concatenated


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
