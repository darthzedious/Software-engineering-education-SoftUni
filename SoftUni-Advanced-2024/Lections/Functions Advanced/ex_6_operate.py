def operate(operator, *args):
    if not args:
        raise ValueError("At least one number is required")

    result = args[0]

    if operator == "+":
        for num in args[1:]:
            result += num
    elif operator == "-":
        for num in args[1:]:
            result -= num
    elif operator == "*":
        for num in args[1:]:
            result *= num
    elif operator == "/":
        if 0 in args[1:]:
            raise ValueError("Division by zero is not allowed")
        for num in args[1:]:
            result /= num

    return result

print(operate("+", 1, 2, 3))
