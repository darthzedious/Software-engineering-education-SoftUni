number_of_students = int(input())
name_grade = {}
for _ in range(number_of_students):
    name, grade = input().split()
    grade = float(grade)
    if name not in name_grade.keys():
        name_grade[name] = []
    name_grade[name].append(grade)

for std_name, std_grade in name_grade.items():
    avg_grade = sum(std_grade)/ len(std_grade)
    print(f"{std_name} -> {' '.join([f'{x:.2f}' for x in std_grade])} (avg: {avg_grade:.2f})")
