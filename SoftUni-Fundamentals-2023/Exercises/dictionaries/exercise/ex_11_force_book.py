force_users = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        force_side, force_user = command.split(" | ")
        is_added = False
        for value in force_users.values():
            if force_user in value:
                is_added = True
                break
        if not is_added:
            if force_side not in force_users.keys():
                force_users[force_side] = []
            force_users[force_side].append(force_user)
    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        for value in force_users.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in force_users.keys():
            force_users[force_side] = []
        force_users[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
for force_side, force_user in force_users.items():
    if len(force_user) > 0:
        print(f"Side: {force_side}, Members: {len(force_user)}")
        for member in force_user:
            print(f"! {member}")
