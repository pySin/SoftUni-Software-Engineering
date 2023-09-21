# Password Generator

# Входът се чете от конзолата и се състои от две цели числа n и l в интервала [1…9], по едно на ред.

n = int(input())
l = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for h in range(l):
            for k in range(l):
                for f in range(1, n + 1):
                    if f > i and f > j:
                        print(f"{i}{j}{alphabet[h]}{alphabet[k]}{f}", end=" ")
