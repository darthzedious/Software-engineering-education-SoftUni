from collections import deque
queue = deque()

while True:
    command = input()
    if command == "Paid":
        while queue:
            print(queue.popleft())
    if command == "End":
        break
    if command != "Paid":
        queue.append(command)

print(f"{len(queue)} people remaining.")
