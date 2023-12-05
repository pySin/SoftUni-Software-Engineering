# Party

class Party:

    def __init__(self):
        self.names = []


party_people = Party()

command = input()
while command != "End":
    party_people.names.append(command)

    command = input()


people_going = ", ".join(party_people.names)
print(f"Going: {people_going}")
print(f"Total: {len(party_people.names)}")
