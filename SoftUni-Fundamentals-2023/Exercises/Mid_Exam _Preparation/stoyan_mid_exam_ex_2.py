friend_list = input().split(", ")
blacklist_counter = 0
lost_counter = 0

while True:
    command = input()
    if command == "Report":
        print(f"Blacklisted names: {blacklist_counter}")
        print(f"Lost names: {lost_counter}")
        print(" ".join(friend_list))
        break
    order = command.split()[0]
    if order == "Blacklist":
        name = command.split()[1]
        if name in friend_list:
            friend_list.insert(friend_list.index(name), "Blacklisted")
            friend_list.remove(name)
            print(f"{name} was blacklisted.")
            blacklist_counter += 1
        else:
            print(f"{name} was not found.")
    elif order == "Error":
        index = int(command.split()[1])
        if 0 <= index < len(friend_list) and friend_list[index] != "Blacklisted" and friend_list[index] != "Lost":
            print(f"{friend_list[index]} was lost due to an error.")
            friend_list[index] = "Lost"
            lost_counter += 1
    elif order == "Change":
        index = int(command.split()[1])
        new_name = command.split()[2]
        if 0 <= index < len(friend_list):
            print(f"{friend_list[index]} changed his username to {new_name}.")
            friend_list[index] = new_name
