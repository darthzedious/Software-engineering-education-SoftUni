n = int(input())
for i in range(1, n+1):
    sum_of_digits = 0
    digit = i
    while digit > 0:
        sum_of_digits += digit % 10
        digit = int(digit / 10)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
