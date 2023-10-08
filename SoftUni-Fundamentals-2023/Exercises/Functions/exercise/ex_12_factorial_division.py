def calculate_the_factorial(num1: int, num2: int) -> float:
    num1_factorial = 1
    num2_factorial = 1
    for n in range(1, num1 + 1):
        num1_factorial *= n
    for i in range(1, num2 + 1):
        num2_factorial *= i
    return num1_factorial / num2_factorial


number_one = int(input())
number_two = int(input())
factorial_division = calculate_the_factorial(number_one, number_two)
print(f"{factorial_division:.2f}")
