wagons = [0] * int(input())
while True:
    command = input().split()

    if command[0] == "End":
        print(wagons)
        break

    elif command[0] == "add":
        wagons[-1] += int(command[1])

    elif command[0] == "insert":
        index1 = int(command[1])
        index2 = int(command[2])
        wagons[index1] += index2

    elif command[0] == "leave":
        index1 = int(command[1])
        index2 = int(command[2])
        wagons[index1] -= index2

