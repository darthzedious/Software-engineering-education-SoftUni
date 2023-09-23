number = int(input())

is_prime = True
if number <= 1:
    is_prime = False
for num in range(2, number+1):
    if number % num == 0 and num <= number/2:
        is_prime = False
        break
if is_prime:
    print('True')
else:
    print('False')
