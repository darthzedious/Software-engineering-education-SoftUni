from math import floor


def first_line(x1, y1, x2, y2):
    if abs(x1) + abs(y1) < abs(x2) + abs(y2):
        return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
    return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"


def second_line(z1, q1, z2, q2):
    if abs(z1) + abs(q1) < abs(z2) + abs(q2):
        return f"({floor(z1)}, {floor(q1)})({floor(z2)}, {floor(q2)})"
    return f"({floor(z2)}, {floor(q2)})({floor(z1)}, {floor(q1)})"


def longer_line(first, second):
    if first < second:
        return second
    return first


x1_coordinates = float(input())
y1_coordinates = float(input())
x2_coordinates = float(input())
y2_coordinates = float(input())
z1_coordinates = float(input())
q1_coordinates = float(input())
z2_coordinates = float(input())
q2_coordinates = float(input())
first_sum = abs(floor(x1_coordinates)) \
        + abs(floor(y1_coordinates)) \
        + abs(floor(x2_coordinates)) \
        + abs(floor(y2_coordinates))
second_sum = abs(floor(z1_coordinates)) \
        + abs(floor(q1_coordinates)) \
        + abs(floor(z2_coordinates)) \
        + abs(floor(q2_coordinates))
if first_sum == second_sum:
    print(first_line(x1_coordinates, y1_coordinates, x2_coordinates, y2_coordinates))
else:
    print(longer_line(first_line(x1_coordinates, y1_coordinates, x2_coordinates, y2_coordinates),
                      second_line(z1_coordinates, q1_coordinates, z2_coordinates, q2_coordinates)))
