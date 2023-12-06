# Party 2

class Party:

    def __init__(self):
        self.names = []

    def add_person(self, name):
        self.names.append(name)

    def get_party_info(self):
        party_info = {
            "going": ", ".join(self.names),
            "total": len(self.names)
        }
        return party_info


party_people = Party()


command = input()
while command != "End":
    party_people.add_person(command)

    command = input()


info = party_people.get_party_info()
print(f"Going {info['going']}")
print(f"Total: {info['total']}")

# people_going = ", ".join(party_people.names)
# print(f"Going: {people_going}""")
# print(f"Total: {len(party_people.names)}")

