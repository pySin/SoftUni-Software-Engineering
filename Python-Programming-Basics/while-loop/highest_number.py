# Highest Number
import sys

our_number = str(-sys.maxsize)
biggest_number = -sys.maxsize

while our_number != "Stop":
    if int(our_number) > biggest_number:
        biggest_number = int(our_number)
    our_number = input()

print(biggest_number)
