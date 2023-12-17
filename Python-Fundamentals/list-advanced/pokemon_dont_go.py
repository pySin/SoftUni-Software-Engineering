# Pokemon Don't Go


def remove_index(sequence, index):
    index_value = sequence[index]
    sequence.pop(index)
    new_sequence = []
    for value in sequence:
        if value <= index_value:
            new_sequence.append(value + index_value)
        else:
            new_sequence.append(value - index_value)
    return new_sequence, index_value


pokemon_distances = [int(x) for x in input().split()]


removed_values = 0
while pokemon_distances:

    command = int(input())

    if command < 0:
        pokemon_distances, index_value = remove_index(pokemon_distances, 0)
        pokemon_distances.insert(0, pokemon_distances[-1])
    elif command >= len(pokemon_distances):
        pokemon_distances, index_value = remove_index(pokemon_distances, -1)
        pokemon_distances.append(pokemon_distances[0])
    else:
        pokemon_distances, index_value = remove_index(pokemon_distances, command)

    removed_values += index_value

print(removed_values)
