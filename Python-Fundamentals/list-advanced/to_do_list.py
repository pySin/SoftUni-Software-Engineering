# To DO List

note = input()

notes = []

while note != "End":
    notes.append(note)
    note = input()

notes.sort(key=lambda x: int(x.split("-")[0]))
notes = [note[-1:] for note in notes]
print(notes)
