# Grades

def grades(grade):
    if 2 <= grade < 3:
        return "Fail"
    if 3 <= grade < 3.50:
        return "Poor"
    if 3.50 <= grade < 4.50:
        return "Good"
    if 4.50 <= grade < 5.50:
        return "Very Good"
    if 5.50 <= grade < 6.00:
        return "Excellent"


current_grade = float(input())
grade_evaluate = grades(current_grade)
print(grade_evaluate)
