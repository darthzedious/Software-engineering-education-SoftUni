judge_data = {}
while True:
    command = input()
    if command == "no more time":
        break
    username, contest, points = command.split(" -> ")
    points = int(points)
    if contest not in judge_data.keys():
        judge_data[contest] = {username: points}
    elif username not in judge_data[contest]:
        judge_data[contest][username] = points
    elif points > judge_data[contest][username]:
        judge_data[contest][points] = points

for contest, info in judge_data.items():
    print(f"{contest}: {len(info)} participants")
    sorted_by_points = dict(sorted(info.items(), key=lambda item: (-item[1], item[0])))
    for rank, (name, points) in enumerate(sorted_by_points.items(), start=1):
        print(f"{rank}. {name} <::> {points}")

total_points = {}
for contest, username in judge_data.items():
    for key, value in username.items():
        if key not in total_points:
            total_points[key] = value
        else:
            total_points[key] += value
print("Individual standings:")
sorted_by_points = dict(sorted(total_points.items(), key=lambda item: (-item[1], item[0])))
for rank, (username, points) in enumerate(sorted_by_points.items(), start=1):
    print(f"{rank}. {username} -> {points}")
