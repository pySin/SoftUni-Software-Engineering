# Unique Usernames


n = int(input())
unique_names = set()


for _ in range(n):
    unique_names.add(input())


# print("\n".join(unique_names))
print(*unique_names, sep="\n")
# for name in unique_names:
#     print(name)
