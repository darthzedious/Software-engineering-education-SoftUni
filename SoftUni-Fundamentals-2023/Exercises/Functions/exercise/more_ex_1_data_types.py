def data_types(command_one: str, command_two: int or str) -> int or str:
    if command_one == "int":
        return int(command_two) * 2
    if command_one == "real":
        result = float(command_two) * 1.5
        return f"{result:.2f}"
    if command_one == "string":
        return f"${str(command_two)}$"


data_type_one = input()
data_type_two = input()
print(data_types(data_type_one, data_type_two))
