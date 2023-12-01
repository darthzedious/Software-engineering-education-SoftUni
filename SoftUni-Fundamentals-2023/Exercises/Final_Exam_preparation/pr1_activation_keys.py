raw_activation_key = input()
while True:
    command = input()
    if command == "Generate":
        print(f"Your activation key is: {raw_activation_key}")
        break
    if "Contains" in command:
        cmd, substring = command.split(">>>")
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif "Flip" in command:
        cmd, second_cmd, start_index, end_index = command.split(">>>")
        start_index, end_index = int(start_index), int(end_index)
        part_to_change = ""
        first_part = raw_activation_key[:start_index]
        second_part = raw_activation_key[end_index:]
        if second_cmd == "Upper":
            part_to_change = raw_activation_key[start_index:end_index].upper()
        elif second_cmd == "Lower":
            part_to_change = raw_activation_key[start_index:end_index].lower()
        raw_activation_key = first_part + part_to_change + second_part
        print(raw_activation_key)
    elif "Slice" in command:
        cmd, start_index, end_index = command.split(">>>")
        start_index, end_index = int(start_index), int(end_index)
        first_part = raw_activation_key[:start_index]
        second_part = raw_activation_key[end_index:]
        raw_activation_key = first_part + second_part
        print(raw_activation_key)
