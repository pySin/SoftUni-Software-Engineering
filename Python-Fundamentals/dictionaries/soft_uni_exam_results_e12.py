# SoftUni Exam Results


def soft_uni_results():

    results_dict = {}
    languages_dict = {}
    command = input()

    while command != "exam finished":

        name_result = command.split("-")

        if name_result[1] == "banned":
            banned_keys = []
            for banned_key in results_dict.keys():
                if name_result[0] in banned_key:
                    banned_keys.append(banned_key)
            for remove_record in banned_keys:
                del results_dict[remove_record]
            command = input()
            continue

        unique_name = name_result[0] + "-" + name_result[1]
        student_result = name_result[2]
        if unique_name in results_dict.keys() and results_dict[unique_name] > student_result:
            pass
        else:
            results_dict[unique_name] = student_result

        if name_result[1] in languages_dict.keys():
            languages_dict[name_result[1]] += 1
        else:
            languages_dict[name_result[1]] = 1

        command = input()

    return results_dict, languages_dict


individual_results, language_results = soft_uni_results()

print("Results:")
for name, result in individual_results.items():
    student = name.split("-")[0]
    print(f"{student} | {result}")

print("Submissions:")
for language, submissions in language_results.items():
    print(f"{language} - {submissions}")
