stops = input()
while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {stops}")
        break
    if "Add Stop" in command:
        cmd, index, message = command.split(":")
        index = int(index)
        if index <= len(stops):
            first_part = stops[:index]
            second_part = stops[index:]
            stops = first_part + message + second_part
        print(stops)
    elif "Remove Stop" in command:
        cmd, start_index, end_index = command.split(":")
        start_index, end_index = int(start_index), int(end_index)
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            first_part = stops[:start_index]
            second_part = stops[end_index + 1:]
            stops = first_part + second_part
        print(stops)
    elif "Switch" in command:
        cmd, old_string, new_string = command.split(":")
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)
