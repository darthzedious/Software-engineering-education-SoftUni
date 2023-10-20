groceries_list = input().split("!")
while True:
    command = input()

    if command == "Go Shopping!":
        print(", ".join(groceries_list))
        break

    command_action = command.split()

    if command_action[0] == "Urgent":
        if command_action[1] not in groceries_list:
            groceries_list.insert(0, command_action[1])

    elif command_action[0] == "Unnecessary":
        if command_action[1] in groceries_list:
            groceries_list.remove(command_action[1])

    elif command_action[0] == "Correct":
        if command_action[1] in groceries_list:
            groceries_list[groceries_list.index(command_action[1])] = command_action[2]

    elif command_action[0] == "Rearrange":
        if command_action[1] in groceries_list:
            groceries_list.remove(command_action[1])
            groceries_list.append(command_action[1])
