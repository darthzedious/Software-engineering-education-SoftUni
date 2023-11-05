phonebook = {}
while True:
    command = input()
    if "-" not in command:
        break
    name, number = command.split("-")
    phonebook[name] = number
searches = int(command)
for names in range(searches):
    name = input()
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
