# Take Skip Rope


hidden_message = input()

numbers_list = [int(number) for number in hidden_message if number.isdigit()]
non_numbers_list = [char for char in hidden_message if not char.isdigit()]


take_list = [numbers_list[take] for take in range(len(numbers_list)) if take % 2 == 0]
odd_list = [numbers_list[take] for take in range(len(numbers_list)) if take % 2 != 0]

taken_string = ""
skipped_string = ""

cursor_position = 0

for i in range(len(take_list)):
    current_take = take_list[i]
    current_skip = odd_list[i]

    take_section = non_numbers_list[cursor_position: cursor_position + current_take]
    taken_string += "".join(take_section)
    cursor_position += current_take
    skip_section = non_numbers_list[cursor_position: cursor_position + current_skip]
    skipped_string += "".join(skip_section)
    cursor_position += current_skip

print(taken_string)
