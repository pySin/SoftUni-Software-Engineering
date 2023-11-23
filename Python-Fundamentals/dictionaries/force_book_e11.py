# Force Book 11


def force_book():

    the_book = {}
    command = input()

    while command != "Lumpawaroo":

        if "|" in command:
            side_user = command.split(" | ")
            side = side_user[0]
            user = side_user[1]

            is_found = False
            for current_side in the_book.keys():
                if user in the_book[current_side]:
                    is_found = True
                    command = input()
                    break
            if is_found:
                continue

            if side not in the_book.keys():
                the_book[side] = [user]
            else:
                the_book[side].append(user)

        elif "->" in command:
            side_user = command.split(" -> ")
            side = side_user[1]
            user = side_user[0]
            # print(user)

            for existing_side, current_users in the_book.items():
                if user in current_users:
                    the_book[existing_side].remove(user)
                    the_book[side].append(user)
                    print(f"{user} joins the {side} side!")

            if side in the_book.keys():
                if user in the_book[side]:
                    pass
                else:
                    print(f"{user} joins the {side} side!")
                    the_book[side].append(user)
            else:
                print(f"{user} joins the {side} side!")
                the_book[side] = [user]

        command = input()
    return the_book


for force_name, force_users in force_book().items():
    force_users_count = len(force_users)
    if force_users_count:
        print(f"Side: {force_name}, Members: {force_users_count}")
        for member in force_users:
            print(f"! {member}")
