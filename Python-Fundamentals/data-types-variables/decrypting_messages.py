# Decrypting Messages


key = int(input())
lines = int(input())

message = ""

for i in range(lines):
    letter = input()
    message += chr(ord(letter) + key)

print(message)
