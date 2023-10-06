def calculator(operation, first_num, second_num):
    result = None
    if operation == "multiply":
        result = first_num * second_num
    elif operation == "divide":
        result = int(first_num / second_num)
    elif operation == "add":
        result = first_num + second_num
    elif operation == "subtract":
        result = first_num - second_num
    return result


operation = input()
first_num = int(input())
second_num = int(input())
final_result = calculator(operation, first_num, second_num)
print(final_result)
