def sum_numbers(num1, num2):
    return num1 + num2

def subtract(result, num3):
    return result - num3


def add_and_subtract(num1, num2, num3):
    returned_result = sum_numbers(num1, num2)
    final_result = subtract(returned_result, num3)
    return final_result


number_one = int(input())
number_two = int(input())
number_three = int(input())
print(add_and_subtract(number_one, number_two, number_three))
