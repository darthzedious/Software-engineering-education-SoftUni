from collections import deque

time_needed = deque([int(x) for x in input().split()])
number_of_tasks = [int(x) for x in input().split()]

duck_types = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while time_needed and number_of_tasks:
    time = time_needed.popleft()
    task = number_of_tasks.pop()

    multiplied = time * task

    if 0 <= multiplied <= 60:
        duck_types["Darth Vader Ducky"] += 1
    elif 61 <= multiplied <= 120:
        duck_types["Thor Ducky"] += 1
    elif 121 <= multiplied <= 180:
        duck_types["Big Blue Rubber Ducky"] += 1
    elif 181 <= multiplied <= 240:
        duck_types["Small Yellow Rubber Ducky"] += 1
    elif multiplied > 240:
        task -= 2
        number_of_tasks.append(task)
        time_needed.append(time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print('\n'.join(f"{key}: {value}" for key, value in duck_types.items()))
