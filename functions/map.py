marks = [65,77,98,86,34,66]
def grade(marks):
    if marks >= 90:
        return 'A'
    elif 80 <= marks <= 90:
        return 'B'
    elif 70 <= marks <= 80:
        return 'C'
    elif 60 <= marks <= 70:
        return 'D'
    else:
        return 'F'
grades = map(grade,marks)
print("Exam Scores:",marks)
print("Grade:",next(grades))    
print("Grade:",list(grades))