n = int(input())

for num in range(n):
    text = input()
    is_pure_string = True
    for i in text:
        if i in (".", ",", "_"):
            print(f'{text} is not pure!')
            is_pure_string = False
            break
    if is_pure_string:
        print(f'{text} is pure.')

