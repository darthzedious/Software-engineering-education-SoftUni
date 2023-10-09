def multiplication_sign(num1: int, num2: int, num3: int) -> str:
    if num1 < 0 < num3 and num2 < 0:
        return "positive"
    elif num1 < 0 < num2 and num3 < 0:
        return "positive"
    elif num1 > 0 > num2 and num3 < 0:
        return "positive"
    elif num1 < 0 or num2 < 0 or num3 < 0:
        return "negative"
    elif num1 > 0 and num2 > 0 and num3 > 0:
        return "positive"
    elif num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"


number_one = int(input())
number_two = int(input())
number_three = int(input())
print(multiplication_sign(number_one, number_two, number_three))
