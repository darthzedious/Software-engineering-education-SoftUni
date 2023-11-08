points_data = {}
language_data = {}
while True:
    command = input()
    if command == "exam finished":
        break
    if "banned" not in command:
        username, language, points = command.split("-")
        points = int(points)
        if username not in points_data.keys():
            points_data[username] = points
        else:
            if points > points_data[username]:
                points_data[username] = points
        if language not in language_data.keys():
            language_data[language] = []
        language_data[language].append(points)
    else:
        username = command.split("-")[0]
        if username in points_data.keys():
            points_data.pop(username)

print("Results:")
for name, points in points_data.items():
    print(f"{name} | {points}")
print("Submissions:")
for language, submissions in language_data.items():
    print(f"{language} - {len(submissions)}")
