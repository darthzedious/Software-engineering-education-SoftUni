number_of_rows = int(input())
direction = input()

if direction == 'u':
    for i in range(number_of_rows):
        for j in range(number_of_rows - 1):
            print(end='')
        for j in range(i+1):
            print('*', end='')
        print()
elif direction == 'd':
    for i in range(number_of_rows, 0, -1):
        for j in range(number_of_rows + 1):
            print(end='')
        for j in range(i):
            print('*', end='')
        print()
