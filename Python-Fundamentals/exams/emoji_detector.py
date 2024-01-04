# Emoji Detector
import re


def find_threshold(source_text):
    pattern = r"-*\d"
    result = [int(x) for x in re.findall(pattern, source_text)]
    cool_threshold = 1
    for num in result:
        # if cool_threshold == 0:
        #     cool_threshold = num
        # else:
        cool_threshold *= num
    print(f"Cool threshold: {cool_threshold}")
    return cool_threshold
    # cool_threshold = 0
    # digits = []
    # for char in source_text:
    #     if char.isdigit():
    #         digits.append(int(char))
    #         if cool_threshold == 0:
    #             cool_threshold = int(char)
    #             continue
    #         cool_threshold *= int(char)
    # print(f"Cool threshold: {cool_threshold}")
    # return cool_threshold


def emojis(source_text):
    pattern = r"((::|\*\*)([A-Z][a-z]{2,})\2)"
    results = [x[0] for x in re.findall(pattern, source_text)]
    return results


def cool_emojis(valid_emojis, cool_threshold):
    the_cool_emojis = []
    for emoji in valid_emojis:
        emoji_result = sum([ord(x) for x in emoji[2:-2]])
        if emoji_result >= cool_threshold:
            the_cool_emojis.append(emoji)
    return the_cool_emojis


def call_functions():
    source_text = input()
    cool_threshold = find_threshold(source_text)

    valid_emojis = emojis(source_text)
    the_cool_emojis = cool_emojis(valid_emojis, cool_threshold)
    cool_emojis_phrase = '\n' + '\n'.join([x for x in the_cool_emojis])
    print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:{cool_emojis_phrase}")


if __name__ == "__main__":
    call_functions()
