number_of_commands = int(input())
users = {}
for i in range(number_of_commands):
    command = input().split()
    if command[0] == "register":
        username = command[1]
        license_plate_number = command[2]
        if username not in users.keys():
            users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    else:
        username = command[1]
        if username not in users.keys():
            print(f"ERROR: user {username} not found")
        else:
            users.pop(username)
            print(f"{username} unregistered successfully")

for username, license_plate_number in users.items():
    print(f"{username} => {license_plate_number}")
