lines = int(input())

is_balanced = True
last_bracket = ''
for _ in range(0, lines):
    character = input()
    if character not in ['(', ')']:
        continue

    if last_bracket == '' and character == ')' or last_bracket == character:
        is_balanced = False
        break

    last_bracket = character

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
