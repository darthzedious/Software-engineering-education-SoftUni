followers = {}
while True:
    command = input()
    if command == "Log out":
        break
    if "New follower" in command:
        cmd, username = command.split(": ")
        if username not in followers.keys():
            followers[username] = [0, 0]
    elif "Like" in command:
        cmd, username, count = command.split(": ")
        count = int(count)
        if username not in followers.keys():
            followers[username] = [count, 0]
        else:
            followers[username][0] += count
    elif "Comment" in command:
        cmd, username = command.split(": ")
        if username not in followers.keys():
            followers[username] = [0, 1]
        else:
            followers[username][1] += 1
    elif "Blocked" in command:
        cmd, username = command.split(": ")
        if username not in followers.keys():
            print(f"{username} doesn't exist.")
        else:
            followers.pop(username)
print(f"{len(followers)} followers")
for username, info in followers.items():
    print(f"{username}: {sum(info)}")
