# Five Component Marking 3

# Step 1 we start by collecting the student exam number or Stop to exit
student_exam_number = input("Enter exam number or Stop to exit: \n")
exam_list = []

while len(student_exam_number) < 3:  # Corrected the condition
    print("Enter a valid exam number!")
    student_exam_number = input("\nEnter exam number or Stop to exit: \n")
    if student_exam_number == "Stop":
        break

# Step 2 we start by collecting the exam scores
ier_vowels = input("Enter ier vowel mark (1-99): ")
while True:
    if ier_vowels.isnumeric() and int(ier_vowels) in range(1, 100):
        ier_vowels = float(ier_vowels)
        break
    else:
        ier_vowels = input("Enter a valid mark between 1 and 99!")

palatalisation = input("Enter palatalisation mark (1-99): ")
while True:
    if palatalisation.isnumeric() and int(palatalisation) in range(1, 100):
        palatalisation = float(palatalisation)
        break
    else:
        palatalisation = input("Enter a valid mark between 1 and 99!")

comparative_part = input("Enter comparative part mark (1-99): ")
while True:
    if comparative_part.isnumeric() and int(comparative_part) in range(1, 100):
        comparative_part = float(comparative_part)
        break
    else:
        comparative_part = input("Enter a valid mark between 1 and 99!")


morphological_analysis = input("Enter morphological_analysis mark (1-99): ")
while True:
    if morphological_analysis.isnumeric() and int(morphological_analysis) in range(1, 100):
        morphological_analysis = float(morphological_analysis)
        break
    else:
        morphological_analysis = input("Enter a valid mark between 1 and 99!")

commentary_essay = input("Enter commentary essay mark (1-99): ")
while True:
    if commentary_essay.isnumeric() and int(commentary_essay) in range(1, 100):
        commentary_essay = float(commentary_essay)
        break
    else:
        commentary_essay = input("Enter a valid mark between 1 and 99!")

while student_exam_number != "Stop":

    general_evaluation = (ier_vowels * 0.10) + (palatalisation * 0.10) + (comparative_part * 0.20) \
                         + (morphological_analysis * 0.20) + (commentary_essay * 0.40)

    print(
        f"Student with exam number {student_exam_number} final mark: {general_evaluation:.2f}")  # Removed unnecessary space
    exam_list.append((student_exam_number, general_evaluation))

    student_exam_number = input("\nEnter exam number or Stop to exit: \n")

    while len(student_exam_number) < 3:  # Corrected the condition
        print("You should enter a correct exam number:")  # Removed unnecessary f-string
        student_exam_number = input("\nEnter exam number or Stop to exit: \n")
        if student_exam_number == "Stop":
            break

    if student_exam_number == "Stop":
        break

    ier_vowels = input("Enter ier vowel mark (1-99): ")
    while True:
        if ier_vowels.isnumeric() and int(ier_vowels) in range(1, 100):
            ier_vowels = float(ier_vowels)
            break
        else:
            ier_vowels = input("Enter a valid mark between 1 and 99!")

    palatalisation = input("Enter palatalisation mark (1-99): ")
    while True:
        if palatalisation.isnumeric() and int(palatalisation) in range(1, 100):
            palatalisation = float(palatalisation)
            break
        else:
            palatalisation = input("Enter a valid mark between 1 and 99!")

    comparative_part = input("Enter comparative part mark (1-99): ")
    while True:
        if comparative_part.isnumeric() and int(comparative_part) in range(1, 100):
            comparative_part = float(comparative_part)
            break
        else:
            comparative_part = input("Enter a valid mark between 1 and 99!")

    morphological_analysis = input("Enter morphological analysis mark (1-99): ")
    while True:
        if morphological_analysis.isnumeric() and int(morphological_analysis) in range(1, 100):
            morphological_analysis = float(morphological_analysis)
            break
        else:
            morphological_analysis = input("Enter a valid mark between 1 and 99!")

    commentary_essay = input("Enter commentary essay mark (1-99): ")
    while True:
        if commentary_essay.isnumeric() and int(commentary_essay) in range(1, 100):
            commentary_essay = float(commentary_essay)
            break
        else:
            commentary_essay = input("Enter a valid mark between 1 and 99!")

print("Exam list:")
for student_number, mark in exam_list:
    print(f"Student number: {student_number}, Mark: {mark:.2f}")
