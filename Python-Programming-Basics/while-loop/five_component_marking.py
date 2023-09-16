# Five Component Marking

student_exam_number = input("Enter exam number or Stop to exit: \n")
while len(str(student_exam_number)) < 3:  # Frequent mistake
    print(f"Enter a valid exam number!")
    student_exam_number = input("\nEnter exam number or Stop to exit: \n")
    if student_exam_number == "Stop":
        break


ier_vowels = float(input("Enter ier vowel mark: "))
palatalisation = float(input("Enter palatalisation mark: "))
comparative_part = float(input("Enter comparative part mark: "))
morphological_analysis = float(input("Enter morphological analysis mark: "))
commentary_essay = float(input("Enter commentary essay mark: "))


while student_exam_number != "Stop":

    general_evaluation = (ier_vowels * 0.10) + (palatalisation * 0.10) + (comparative_part * 0.20) \
                         + (morphological_analysis * 0.20) + (commentary_essay * 0.40)

    print(f"Student with exam number {student_exam_number} final mark: {general_evaluation :.2f}")

    student_exam_number = input("\nEnter exam number or Stop to exit: \n")

    while len(str(student_exam_number)) < 3:
        print(f"You should enter a correct exam number:")
        student_exam_number = input("\nEnter exam number or Stop to exit: \n")
        if student_exam_number == "Stop":
            break

    if student_exam_number == "Stop":
        break

    ier_vowels = float(input("Enter ier vowel mark: "))
    palatalisation = float(input("Enter palatalisation mark: "))
    comparative_part = float(input("Enter comparative part mark: "))
    morphological_analysis = float(input("Enter morphological analysis mark: "))
    commentary_essay = float(input("Enter commentary essay mark: "))
