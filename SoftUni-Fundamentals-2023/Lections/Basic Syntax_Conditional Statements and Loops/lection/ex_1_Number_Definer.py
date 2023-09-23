roll = int(input())

for number in range(roll):
    number = float(input())
    if number == 0:
        print('zero')
        continue
    elif number > 0:
        if number < 1:
            print('small positive')
            continue
        elif number > 1000000:
            print('large positive')
            continue
        else:
            print('positive')
            continue
    elif number < 0:
        if abs(number) < 1:
            print('small negative')
            continue
        elif abs(number) > 1000000:
            print('large negative')
            continue
        else:
            print('negative')
            continue


