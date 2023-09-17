# Five Component Marking 4

while True:
    student_exam_number = input("Enter exam number or Stop to exit: \n")

    if student_exam_number == "Stop":
        break

    if len(student_exam_number) < 3:
        print("Enter a valid exam number!")
        continue

    marks = {}
    for mark_type in ["ier vowel", "palatalisation", "comparative part", "morphological analysis", "commentary essay"]:
        while True:
            try:
                value = float(input(f"Enter {mark_type} mark: "))
                if 1 <= value <= 99:
                    marks[mark_type] = value
                    break
                else:
                    print(f"Enter a valid mark between 1 and 99.")
            except ValueError:
                print("Enter a valid numeric value.")

    general_evaluation = (marks["ier vowel"] * 0.10) + (marks["palatalisation"] * 0.10) + (
                marks["comparative part"] * 0.20) \
                + (marks["morphological analysis"] * 0.20) + (marks["commentary essay"] * 0.40)

    print(f"Student with exam number {student_exam_number} final mark: {general_evaluation:.2f}")
