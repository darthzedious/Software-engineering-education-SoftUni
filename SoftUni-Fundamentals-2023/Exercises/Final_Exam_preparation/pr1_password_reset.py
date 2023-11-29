initial_password = input()
initial_password_2 = ""
while True:
    command = input()
    if command == "Done":
        print(f"Your password is: {initial_password}")
        break
    if "TakeOdd" in command:
        for letter in range(len(initial_password)):
            if letter % 2 != 0:
                initial_password_2 += initial_password[letter]
        initial_password = initial_password_2
        print(initial_password)
    elif "Cut" in command:
        cmd, length, index = command.split()
        index, length = int(index), int(length)
        substring_first = initial_password[:length]
        substring_second = initial_password[length+index:]
        initial_password = substring_first + substring_second
        print(initial_password)
    elif "Substitute" in command:
        cmd, substring, substitute = command.split()
        if substring in initial_password:
            initial_password = initial_password.replace(substring, substitute)
            print(initial_password)
        else:
            print(f"Nothing to replace!")
