# Challenge The Wedding

# ⦁	Броя клиенти мъже - цяло число в интервала [1...100]
# ⦁	Броя клиенти жени - цяло число в интервала [1...100]
# ⦁	Максималният брой маси - цяло число в интервала [1...100]

male_clients = int(input())
f_male_clients = int(input())
tables_available = int(input())

tables = 0
is_tables_over = False
for i in range(1, male_clients + 1):
    for j in range(1, f_male_clients + 1):
        tables += 1
        # print(str("Available: " + str(tables_available) + " " + "Taken: " + str(tables)))
        print(f"({i} <-> {j})", end=" ")
        if tables == tables_available:
            is_tables_over = True
            break
    if is_tables_over:
        break

        # print(f"({i} <-> {j})", end=" ")
        # print(f"({i} <-> {j})", end=" ")
        # print(f"({i} <-> {j})", end=" ")
