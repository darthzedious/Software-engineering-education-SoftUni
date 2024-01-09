from sys import maxsize
stack = []
n = int(input())
max_number = 0
min_number = maxsize
for turn in range(n):
    command = input()
    if command.startswith("1"):
        cmd, number = command.split()
        number = int(number)
        stack.append(number)
    elif stack:
        if command == "2":
            stack.pop()
        elif command == "3":
            for x in range(len(stack)):
                if stack[x] > max_number:
                    max_number = stack[x]
            print(max_number)
        elif command == "4":
            for x in range(len(stack)):
                if stack[x] < min_number:
                    min_number = stack[x]
            print(min_number)

while stack:
    print(stack.pop(), end="")
    if stack:
        print(", ", end="")
