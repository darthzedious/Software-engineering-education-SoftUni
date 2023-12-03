text = input()
while True:
    command = input()
    if command == "Finish":
        break
    if "Replace" in command:
        cmd, current_char, new_char = command.split()
        text = text.replace(current_char, new_char)
        print(text)
    elif "Cut" in command:
        cmd, start_index, end_index = command.split()
        start_index, end_index = int(start_index), int(end_index)
        if start_index in range(len(text)) and end_index in range(len(text)):
            first_part = text[:start_index]
            second_part = text[end_index+1:]
            text = first_part + second_part
            print(text)
        else:
            print("Invalid indices!")
    elif "Make" in command:
        cmd, upper_lower = command.split()
        if upper_lower == "Upper":
            text = text.upper()
            print(text)
        elif upper_lower == "Lower":
            text = text.lower()
            print(text)
    elif "Check" in command:
        cmd, check = command.split()
        if check in text:
            print(f"Message contains {check}")
        else:
            print(f"Message doesn't contain {check}")
    elif "Sum" in command:
        cmd, start_index, end_index = command.split()
        start_index, end_index = int(start_index), int(end_index)
        if start_index in range(len(text)) and end_index in range(len(text)):
            substring = text[start_index:end_index + 1]
            ascii_sum = sum(list(ord(x) for x in substring))
            print(ascii_sum)
        else:
            print("Invalid indices!")
