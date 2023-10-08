def odd_and_even_sum(number: str):
    even_sum = 0
    odd_sum = 0
    for num in number:
        if int(num) % 2 == 0:
            even_sum += int(num)
        else:
            odd_sum += int(num)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


single_number = input()
print(odd_and_even_sum(single_number))
