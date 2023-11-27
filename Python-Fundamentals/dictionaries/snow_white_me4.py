# Snow White


def get_dwarf_data():

    dwarf_data = {}
    command = input()

    while command != "Once upon a time":

        command = command.split(" <:> ")
        dwarf_name = command[0]
        dwarf_hat_color = command[1]
        dwarf_physics = int(command[2])
        color_name = "(" + dwarf_hat_color + ")" + " " + dwarf_name
        if color_name not in dwarf_data:
            dwarf_data[color_name] = {dwarf_hat_color: dwarf_physics}
        else:
            if dwarf_data[color_name][dwarf_hat_color] < dwarf_physics:
                dwarf_data[color_name][dwarf_hat_color] = dwarf_physics

        command = input()
    return dwarf_data


def sort_dwarfs(dwarf_data):
    dwarf_list = []

    for key, value in dwarf_data.items():
        for key_2, value_2 in value.items():
            dwarf_list.append([key, key_2, value_2])
    colors_list = [color[1] for color in dwarf_list]
    # print(colors_list)
    dwarf_list = sorted(dwarf_list, key=lambda x: colors_list.count(x[1]), reverse=True)
    dwarf_list = sorted(dwarf_list, key=lambda x: x[2], reverse=True)
    # print(dwarf_list)
    for name, color, physics in dwarf_list:
        print(f"{name} <-> {physics}")


def call_functions():
    dwarf_data = get_dwarf_data()
    sort_dwarfs(dwarf_data)


if __name__ == "__main__":
    call_functions()
