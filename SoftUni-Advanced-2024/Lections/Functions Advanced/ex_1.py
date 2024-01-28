def multiply(*args):
    n = 1
    for i in args:
        n *= i
    return n


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
