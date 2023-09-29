gifts = input().split(' ')
while True:
    command = input()
    if command == "No Money":
        break
    command_as_list = command.split(" ")
    order_command = command_as_list[0]
    command_gifts = command_as_list[1]
    for gift in gifts:
        if order_command == "OutOfStock" and command_as_list[1] in gifts:
            gifts.insert(gifts.index(command_as_list[1]), 'None')
            gifts.remove(command_as_list[1])
    if order_command == "Required":
        if 0 <= int(command_as_list[2]) < len(gifts):
            gifts[int(command_as_list[2])] = command_as_list[1]
    if order_command == "JustInCase":
        gifts[-1] = command_as_list[1]
for gift in gifts:
    if "None" in gifts:
        gifts.remove("None")
print(" ".join(str(x) for x in gifts))
