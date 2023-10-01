sequence_of_numbers = input().split(" ")
code = input()
expected_message = []
for part in sequence_of_numbers:
    part_sum = 0
    for element in part:
        part_sum += int(element)

    part_sum %= len(code)
    expected_message.append(code[part_sum])
    code = code.replace(code[part_sum], "", 1)
print("".join(expected_message))
