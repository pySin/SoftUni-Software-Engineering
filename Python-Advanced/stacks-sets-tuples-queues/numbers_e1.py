# Numbers


first_numbers = set((int(x) for x in input().split()))
second_numbers = set((int(x) for x in input().split()))

n = int(input())

for _ in range(n):

    command = input().split()
    action_type = command[0]

    if action_type == "Add":
        collection = command[1]
        numbers_to_add = set((int(x) for x in command[2:]))
        if collection == "First":
            first_numbers = first_numbers.union(numbers_to_add)
        elif collection == "Second":
            second_numbers = second_numbers.union(numbers_to_add)
    elif action_type == "Remove":
        collection = command[1]
        numbers_to_remove = [int(x) for x in command[2:]]
        if collection == "First":
            first_numbers.difference_update(numbers_to_remove)
        elif collection == "Second":
            second_numbers.difference_update(numbers_to_remove)
    elif action_type == "Check":
        if first_numbers.issuperset(second_numbers) or second_numbers.issuperset(first_numbers):
            # print(first_numbers.issuperset(second_numbers) or second_numbers.issuperset(first_numbers))
            print("True")
        else:
            print("False")

print(*sorted(first_numbers), sep=", ")
print(*sorted(second_numbers), sep=", ")
