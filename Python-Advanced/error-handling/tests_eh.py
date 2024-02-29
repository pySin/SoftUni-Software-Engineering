# Tests


# print("Test")

# a = input().split()
#
# print(a[2])

# print("go" + 6)

# print(2 + "2")

# a = {"a": 1, "b": 3}
#
# key = input()
# print(a.get(key))

# -- TypeError

# print(len(2))

# -- ValueError

# print(int("bd"))

# -- Catching Exceptions(Try-Except-Finally

# a = [int(el) for el in input().split()]
#
# if 4 in range(len(a)):
#     print(a[4])
# else:
#     print("Invalid index")

# --
# a = [int(el) for el in input().split()]
#
# index = int(input())
#
# try:
#     print(a[index])
# except IndexError:
#     print("Invalid index")
#
# print("Later!")

# -- Handle improper input

# while True:
#     try:
#         number = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Ooops... This is not a valid error. Try again!")

# -- Multiple Errors

# a = [int(el) for el in input().split()]
#
#
# try:
#     index = int(input())
#     print(a[index])
# except IndexError as ex:
#     print(f"Invalid index for length of {len(a)}")
# except ValueError:
#     print(f"You must enter a number!")
# else:
#     print("Else clause: everything went well!")
# finally:
#     print("Finally statement!")

# -- Try Finally

# try:
#     print(int(input()))  # Rises Error
# finally:
#     print("This always prints")

# -- Update Set with list

# a = {1, 4}
# a.update([1, 2, 3])
# print(a)


# -- * Error Handling Exercise

# test_dict = {"a": 1, "b": 2, "c": 3}
# test_index = [1, 2, 3]
#
# letter = input()
#
# try:
#     x = 2 / 0
#     print(test_index[3])
#     print(test_dict[letter])
# except Exception as e:
#     print(f"We have this error: {e}")
#     print(f"Error type: {type(e)}")
# except KeyError:
#     print("Key Error")
# except IndexError:
#     print("Index Error")
# except ZeroDivisionError as e:
#     print(f"Zero Division Error: {e}")
# else:
#     print("Everything went well")
# finally:
#     print("Program finished")

# --

# class MyError(Exception):
#     pass

# Error raised in the TRY section is not raised

# def check_try():
#     try:
#         x = int("x")
#         raise IndexError
#     except Exception as e:
#         print(e)
#     finally:
#         print("End of business")
#
#
# if __name__ == "__main__":
#     check_try()


