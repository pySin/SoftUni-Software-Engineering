# Strange Zoo

animal_list = []
for _ in range(3):
    animal = input()
    animal_list.append(animal)

animal_list[0], animal_list[2] = animal_list[2], animal_list[0]
print(animal_list)
