key = int(input())
message = ''
number_of_lines = int(input())
for i in range(number_of_lines):
    letter = input()
    letter_in_numbers = ord(letter)
    final_letter = chr(letter_in_numbers + key)
    message += final_letter
print(message)
