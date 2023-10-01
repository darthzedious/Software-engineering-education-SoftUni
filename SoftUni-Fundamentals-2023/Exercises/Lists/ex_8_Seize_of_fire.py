type_and_value = input().split("#")
amount_of_water = int(input())
high = range(81, 125+1)
medium = range(51, 80+1)
low = range(1, 50+1)
effort = 0
valid_cells = []
for data in type_and_value:
    cell_is_valid = False
    type, value = data.split(" = ")
    value = int(value)
    if type == "High" and value in high:
        cell_is_valid = True
    elif type == "Medium" and value in medium:
        cell_is_valid = True
    elif type == "Low" and value in low:
        cell_is_valid = True

    if cell_is_valid:
        if amount_of_water >= value:
            amount_of_water -= value
            valid_cells.append(value)
            effort += value * 0.25

print(f"Cells:")
for cells in valid_cells:
    print(f"- {cells}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(int(cells) for cells in valid_cells)}")
