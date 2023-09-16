# Find the 100

# Using a while loop, len function, an if statement and the str() function; iterate through the given
# list and if there is a 100, assign a notification message to the variable my_message with the index of 100.
# i.e.: "There is a 100 at index no: 5"

lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]

current_index = 0
our_index = None
while current_index < len(lst):
    if lst[current_index] == 100:
        our_index = current_index
        print(f"There is a 100 at index no: {our_index}")
        break
    current_index += 1
