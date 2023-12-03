password = input()
while True:
    command = input()
    if command == "End":
        break
    if "Translate" in command:
        cmd, char, replacement = command.split()
        if char in password:
            password = password.replace(char, replacement)
            print(password)
    elif "Includes" in command:
        cmd, substring = command.split()
        if substring in password:
            print("True")
        else:
            print("False")
    elif "Start" in command:
        cmd, substring = command.split()
        if password.startswith(substring):
            print("True")
        else:
            print("False")
    elif "Lowercase" in command:
        password = password.lower()
        print(password)
    elif "FindIndex" in command:
        cmd, char = command.split()
        last_occurrence = password.rfind(char)
        print(last_occurrence)

    elif 'Remove' in command:
        cmd, start_index, count = command.split()
        start_index, count = int(start_index), int(count)
        substring = password[start_index:start_index + count]
        password = password.replace(substring, "")
        print(password)
