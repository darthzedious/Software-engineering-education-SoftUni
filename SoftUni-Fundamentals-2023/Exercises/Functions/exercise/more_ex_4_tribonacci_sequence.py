def tribonacci_main(number):
    if (number == 0 or number == 1 or number == 2):
        return 0
    elif (number == 3):
        return 1
    else:
        return (tribonacci_main(number - 1) +
                tribonacci_main(number - 2) +
                tribonacci_main(number - 3))


def final(n):
    for i in range(3, n+3):
        print(tribonacci_main(i), "", end="")


# Driver code
attempt = int(input())
final(attempt)
