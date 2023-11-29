# Word Synonyms


def synonyms(count):

    synonyms_list = {}

    for i in range(count):
        word = input()
        synonym = input()
        if word in synonyms_list.keys():
            synonyms_list[word].append(synonym)
        else:
            synonyms_list[word] = [synonym]
    return synonyms_list


if __name__ == "__main__":
    count_synonyms = int(input())
    for key, value in synonyms(count_synonyms).items():
        print(f"{key} - {', '.join(value)}")
