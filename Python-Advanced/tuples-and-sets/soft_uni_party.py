# SoftUni Party


n = int(input())

reservation_set = set()
attended_set = set()

for _ in range(n):

    reservation = input()
    reservation_set.add(reservation)

command = input()
while command != "END":
    attending_guest = command
    
    attended_set.add(attending_guest)
    attended_set.add(attending_guest)
    
    command = input()

non_attended_set = reservation_set - attended_set

print(len(non_attended_set))
for non_attended in sorted(non_attended_set):
    print(non_attended)
