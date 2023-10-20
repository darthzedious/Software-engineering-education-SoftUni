targets_values = [int(target) for target in input().split()]
while True:
    command = input().split()
    if command[0] == "End":
        print("|".join(str(target) for target in targets_values))
        break
    elif command[0] == "Shoot":
        index, power = int(command[1]), int(command[2])
        if index in range(len(targets_values)):
            targets_values[index] -= power
            if targets_values[index] <= 0:
                targets_values.pop(index)
    elif command[0] == "Add":
        index, value = int(command[1]), int(command[2])
        if index in range(len(targets_values)):
            targets_values.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        index, radius = int(command[1]), int(command[2])
        if index in range(len(targets_values)):
            if index - radius in range(len(targets_values)) and index + radius in range(len(targets_values)):
                del targets_values[index - radius: index + radius + 1]
            else:
                print("Strike missed!")
