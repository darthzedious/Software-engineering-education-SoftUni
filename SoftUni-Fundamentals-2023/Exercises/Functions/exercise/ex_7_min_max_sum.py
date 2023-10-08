def min_max_sum(lst_numbers: list):
    return f"The minimum number is {min(lst_numbers)}" "\n"\
           f"The maximum number is {max(lst_numbers)}" "\n"\
           f"The sum number is: {sum(lst_numbers)}"


numbers = list(int(x) for x in input().split(" "))
print(min_max_sum(numbers))
