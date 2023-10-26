chat = []
while True:
    command = input()
    if command == "end":
        print("\n".join(str(x) for x in chat))
        break
    action = command.split()[0]
    if action == "Chat":
        message = command.split()[1]
        chat.append(message)
    if action == "Delete":
        message = command.split()[1]
        if message in chat:
            chat.remove(message)
    if action == "Edit":
        message = command.split()[1]
        edited_version = command.split()[2]
        abc = list(str(i) for i in chat)
        if message in chat:
            if message in chat:
                chat.insert(chat.index(message), edited_version)
                chat.remove(message)
            else:
                chat.insert(chat.index(message), edited_version)
                chat.remove(message)
    if action == "Pin":
        message = command.split()[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)
    if action == "Spam":
        messages = list(str(i) for i in command.split() if i != "Spam")
        for i in range(len(messages)):
            chat.append(messages[i])
