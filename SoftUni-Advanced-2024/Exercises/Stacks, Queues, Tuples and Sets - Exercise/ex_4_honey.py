from collections import deque
working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

operations = {"*": lambda a, b: a * b,
              "/": lambda a, b: a / b if b != 0 else 0,
              "-": lambda a, b: a - b,
              "+": lambda a, b: a + b}
total_honey = 0

while working_bees and nectar:
    bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= bee:
        total_honey += abs(operations[symbols.popleft()](bee, current_nectar))
    else:
        working_bees.appendleft(bee)
print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
