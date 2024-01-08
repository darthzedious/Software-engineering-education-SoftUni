from collections import deque

queue = deque()
liters = int(input())

while True:
    name = input()
    if name == "Start":
        break
    queue.append(name)

while True:
    command = input()
    if command == "End":
        break
    if "refill" not in command:
        command = int(command)
        if liters >= command:
            liters -= command
            print(f"{queue[0]} got water")
            queue.popleft()
        else:
            print(f"{queue[0]} must wait")
            queue.popleft()
    else:
        added_liters = int(command.split()[1])
        liters += added_liters
print(f"{liters} liters left")
