# Electron Distribution

electron_count = int(input())


def place_electrons(number_of_electrons):

    electron_shells = []
    shell = 1
    while number_of_electrons > 0:
        current_shell = 2*shell**2
        if number_of_electrons <= current_shell:
            electron_shells.append(number_of_electrons)
            number_of_electrons -= current_shell
        else:
            electron_shells.append(current_shell)
            number_of_electrons -= current_shell
        shell += 1

    return electron_shells


all_electron_shells = place_electrons(electron_count)
print(all_electron_shells)
