students = {}
all_students = []
searched_course = None
while True:
    command = input()
    if ":" not in command:
        searched_course = command
        break
    name, ID, course = command.split(":")
    all_students.append({"name": name, "ID": ID, "course": course})

for student in all_students:
    if searched_course.startswith(student["course"][0:3]):
        print(f"{student['name']} - {student['ID']}")
