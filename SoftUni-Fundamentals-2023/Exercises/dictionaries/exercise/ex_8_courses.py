students_check = {}
while True:
    command = input()
    if command == "end":
        break
    course_name, student_name = command.split(" : ")
    if course_name not in students_check.keys():
        students_check[course_name] = []
    students_check[course_name].append(student_name)

for course_name, student_name in students_check.items():
    print(f"{course_name}: {len(students_check[course_name])}")
    for names in range(len(students_check[course_name])):
        print(f"-- {students_check[course_name][names]}")
