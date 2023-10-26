# List Manipulator


numbers = [int(number) for number in input().split()]

command = input()

while command != "end":

    instructions = command.split()
    if instructions[0] == "exchange":
        if int(instructions[1]) >= len(numbers) or int(instructions[1]) < 0:
            print("Invalid index")
        else:
            numbers = numbers[int(instructions[1]) + 1:] + numbers[: int(instructions[1]) + 1]
            # print(numbers)
    elif instructions[0] == "max":
        if instructions[1] == "even":
            even_numbers = [num for num in numbers if num % 2 == 0]

            if even_numbers:
                max_even = max(even_numbers)
                for i in range(len(numbers) - 1, - 1, - 1):
                    if numbers[i] == max_even:
                        print(i)
                        break
            else:
                print("No matches")
        elif instructions[1] == "odd":
            odd_numbers = [num for num in numbers if num % 2 != 0]

            if odd_numbers:
                max_odd = max(odd_numbers)
                for i in range(len(numbers) - 1, - 1, - 1):
                    if numbers[i] == max_odd:
                        print(i)
                        break
            else:
                print("No matches")

    elif instructions[0] == "min":
        if instructions[1] == "even":
            even_numbers = [num for num in numbers if num % 2 == 0]

            if even_numbers:
                min_even = min(even_numbers)
                for i in range(len(numbers) - 1, - 1, - 1):
                    if numbers[i] == min_even:
                        print(i)
                        break
            else:
                print("No matches")
        elif instructions[1] == "odd":
            odd_numbers = [num for num in numbers if num % 2 != 0]

            if odd_numbers:
                min_odd = min(odd_numbers)
                for i in range(len(numbers) - 1, - 1, - 1):
                    if numbers[i] == min_odd:
                        print(i)
                        break
            else:
                print("No matches")

    elif instructions[0] == "first":
        if instructions[2] == "even":
            even_numbers = [num for num in numbers if num % 2 == 0]
            if len(numbers) < int(instructions[1]):
                print("Invalid count")
            elif len(even_numbers) <= int(instructions[1]):
                print(even_numbers)
            elif len(even_numbers) > int(instructions[1]):
                print(even_numbers[:int(instructions[1])])

        elif instructions[2] == "odd":
            odd_numbers = [num for num in numbers if num % 2 != 0]
            if len(numbers) < int(instructions[1]):
                print("Invalid count")
            elif len(odd_numbers) <= int(instructions[1]):
                print(odd_numbers)
            elif len(odd_numbers) > int(instructions[1]):
                print(odd_numbers[:int(instructions[1])])

    elif instructions[0] == "last":
        if instructions[2] == "even":
            even_numbers = [num for num in numbers if num % 2 == 0]
            # even_numbers = even_numbers[::-1]

            if len(numbers) < int(instructions[1]):
                print("Invalid count")
            elif len(even_numbers) < int(instructions[1]):
                print(even_numbers)
            elif len(even_numbers) >= int(instructions[1]):
                print(even_numbers[-int(instructions[1]):])

        elif instructions[2] == "odd":
            odd_numbers = [num for num in numbers if num % 2 != 0]
            # odd_numbers = odd_numbers[::-1]
            if len(numbers) < int(instructions[1]):
                print("Invalid count")
            elif len(odd_numbers) < int(instructions[1]):
                print(odd_numbers)
            elif len(odd_numbers) >= int(instructions[1]):
                # print(f"Last Odd: {odd_numbers}")
                print(odd_numbers[-int(instructions[1]):])

    command = input()

print(numbers)
