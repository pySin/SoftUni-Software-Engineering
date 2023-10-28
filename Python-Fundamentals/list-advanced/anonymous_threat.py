# Anonymous Threat


def anonymous_string(string):
    code_words = string.split()
    print("Code Words: " + str(code_words))

    command = input()

    while command != "3:1":

        instructions = command.split()
        # print("Instructions:" + str(instructions))
        if instructions[0] == "merge":
            # print(instructions)
            merged_string = ""

            for i in range(int(instructions[1]), int(instructions[2])):
                if int(instructions[1]) >= len(code_words):
                    break
                # print(code_words)
                # print(i)
                merged_string += code_words[i]
                print("Merged: " + merged_string)
            code_words = code_words[:int(instructions[1])] + code_words[int(instructions[2]):]
            code_words.insert(int(instructions[1]), merged_string)
            print(code_words)
        command = input()
    return code_words


def call_functions():
    string = input()
    codes = anonymous_string(string)
    print(codes)


if __name__ == "__main__":
    call_functions()
