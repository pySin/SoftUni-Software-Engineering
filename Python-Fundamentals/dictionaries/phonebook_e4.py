# Phonebook


def phonebook():

    contacts = {}

    while True:
        get_phone = input()

        if "-" not in get_phone:
            number_of_searches = int(get_phone)
            break

        get_phone = get_phone.split("-")
        name = get_phone[0]
        number = get_phone[1]
        contacts[name] = number

    for i in range(number_of_searches):
        search_name = input()
        if search_name in contacts.keys():
            print(f"{search_name} -> {contacts[search_name]}")
        else:
            print(f"Contact {search_name} does not exist.")


phonebook()
