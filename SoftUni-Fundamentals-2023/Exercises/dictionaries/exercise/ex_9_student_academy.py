number_of_students = int(input())
students_data = {}
average_grades = {}
for students in range(number_of_students):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_data.keys():
        students_data[student_name] = []
    students_data[student_name].append(student_grade)
for student_name, student_grade in students_data.items():
    average_grade = sum(student_grade) / len(student_grade)
    if average_grade >= 4.50:
        if student_name not in average_grades.keys():
            average_grades[student_name] = average_grade
for student_name, average_grade in average_grades.items():
    print(f"{student_name} -> {average_grade:.2f}")

#filtered_students = {student: avg for student, avg in students_data.items() if avg >= 4.50} => dict comprehention