def upper_part(number):
    for star in range(1, number + 1):
        print(" " * (number - star), '* ' * star)


def lower_part(number):
    for star in range(number - 1, -1, -1):
        print(" " * (number - star), '* ' * star)


n = int(input())
upper_part(n)
lower_part(n)
