# Age Assignment


def age_assignment(*args, **kwargs):
    name_age_pairs = []
    for key, age in kwargs.items():
        for name in args:
            if name[0] == key:
                name_age_pairs.append(f"{name} is {age} years old.")
    return "\n".join(sorted(name_age_pairs))


print(age_assignment("Peter", "George", G=26, P=19))
print()
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
