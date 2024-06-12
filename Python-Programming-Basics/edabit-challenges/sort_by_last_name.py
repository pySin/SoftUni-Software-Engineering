# Sort by Last Name


def last_name_lensort(names):
    def sort_by_length(name):
        second_name = name.split()[1]
        return len(second_name)

    names.sort(reverse=True, key=sort_by_length)  # [1, 1, 2, 4, 5, 5, 5, 7]
    return names


all_names = [
  "Jennifer Figueroa",
  "Heather Mcgee",
  "Amanda Schwartz",
  "Nicole Yoder",
  "Melissa Hoffman",
  "David Hasselhoff",
  "Chen Lee"
]

sorted_names = last_name_lensort(all_names)
print(sorted_names)
