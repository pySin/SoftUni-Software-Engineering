# Smallest number
import sys

our_number = str(sys.maxsize)
smallest_number = sys.maxsize

while our_number != "Stop":
    if int(our_number) < smallest_number:
        smallest_number = int(our_number)
    our_number = input()

print(smallest_number)
