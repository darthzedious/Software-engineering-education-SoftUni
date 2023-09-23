number_of_messages = int(input())

for i in range(number_of_messages):
    number = int(input())
    if number == 88:
        print('Hello')
        continue
    elif number == 86:
        print('How are you?')
        continue
    elif number != 88 and number < 88 or number != 86 and number < 88:
        print('GREAT!')
        continue
    elif number > 88:
        print("Bye.")
        continue
