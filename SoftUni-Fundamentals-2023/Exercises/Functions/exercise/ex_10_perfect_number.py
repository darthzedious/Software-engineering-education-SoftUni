def perfect_number(number: int) -> str:
    counter = 0
    for num in range(1, number):
        if number % num == 0:
            counter += num
    if counter == number:
        return "We have a perfect number!"
    return "It's not so perfect."


number_try = int(input())
print(perfect_number(number_try))
