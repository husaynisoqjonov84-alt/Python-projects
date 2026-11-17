students = ["James", "Oliver", "William", "Henry", "Jack", "Thomas", "Daniel"]

grades = []
limit = list(range(1, 11))


for student in students:
    grade = int(input(f"The grade of {student}: "))
    
    if grade != "limit":
       print('You can only grade in 1 to 10 grading system!!!')
    
    grades.append(grade)

medium_grade = sum(grades) / len(grades)
max_grade = max(grades)
min_grade = min(grades)

print("Medium grade is >>>", medium_grade)
print("Max grade is >>>", max_grade)
print("Min grade is >>>", min_grade)