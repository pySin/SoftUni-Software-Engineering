# Chat codes


number_of_messages = int(input())

for i in range(number_of_messages):
    current_code = int(input())

    if current_code == 88:
        print("Hello")
    elif current_code == 86:
        print("How are you?")
    elif current_code < 88:
        print("GREAT!")
    else:
        print("Bye.")
