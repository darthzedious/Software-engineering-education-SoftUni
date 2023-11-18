console_input = input()
explosion_counter = 0
final_string = ""
for char in range(len(console_input)):
    if explosion_counter > 0 and console_input[char] != ">":
        explosion_counter -= 1
    elif console_input[char] == ">":
        final_string += console_input[char]
        explosion_counter += int(console_input[char + 1])
    else:
        final_string += console_input[char]
print(final_string)
