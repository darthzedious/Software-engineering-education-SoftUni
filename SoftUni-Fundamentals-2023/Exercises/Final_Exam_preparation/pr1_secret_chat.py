concealed_message = input()
while True:
    command = input()
    if command == "Reveal":
        print(f"You have a new text message: {concealed_message}")
        break
    if "InsertSpace" in command:
        cmd, index = command.split(":|:")
        index = int(index)
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif "Reverse" in command:
        cmd, substring = command.split(":|:")
        if substring in concealed_message:
            replacement = substring[::-1]
            concealed_message = concealed_message.replace(substring, replacement)
            print(concealed_message)
        else:
            print("error")
    elif "ChangeAll" in command:
        cmd, substring, replacement = command.split(":|:")
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
